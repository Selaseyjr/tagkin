// Original soundtrack for the Tagkin walkthrough, synthesised from scratch (no samples, no licences).
// Reads timeline.json (cue times) and writes soundtrack.wav: warm pad + pluck arpeggio + light pulse,
// a Tagkin "signature" chime for intro and outro, and UI sounds synced to taps, typing and alerts.
import fs from "node:fs";

const SR = 44100;
const { cues, end } = JSON.parse(fs.readFileSync(process.argv[2] || "timeline.json", "utf8"));
const DUR = end + 1.5;
const N = Math.ceil(DUR * SR);
const L = new Float32Array(N),
  R = new Float32Array(N);
const mtof = (m) => 440 * 2 ** ((m - 69) / 12);
const add = (i, l, r = l) => {
  if (i >= 0 && i < N) {
    L[i] += l;
    R[i] += r;
  }
};
let seed = 7;
const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647) * 2 - 1;

const introEnd = cues.find((c) => c.type === "whoosh")?.t ?? 5;
const outroAt = cues.find((c) => c.type === "outro")?.t ?? end - 7;
const BPM = 96,
  beat = 60 / BPM,
  bar = beat * 4;

// ---------- pad ----------
const chords = [
  [48, 55, 59, 62, 64],
  [45, 52, 55, 59, 60],
  [41, 48, 52, 55, 57],
  [43, 50, 55, 57, 62],
]; // Cmaj9 Am9 Fmaj9 G6sus
function pad(t0, t1, notes, gain) {
  const a = 1.2,
    r = 1.6,
    i0 = Math.floor(t0 * SR),
    i1 = Math.floor((t1 + r) * SR);
  for (const [k, m] of notes.entries()) {
    const f = mtof(m + 12),
      pan = (k / (notes.length - 1)) * 0.8 - 0.4;
    for (let i = i0; i < i1; i++) {
      const t = i / SR - t0,
        env = Math.min(1, t / a) * (i / SR > t1 ? Math.max(0, 1 - (i / SR - t1) / r) : 1);
      const ph = 2 * Math.PI * f * t;
      const s =
        (Math.sin(ph) + 0.35 * Math.sin(2 * ph * 1.002) + 0.12 * Math.sin(3 * ph * 0.998)) *
        (0.8 + 0.2 * Math.sin(2 * Math.PI * 0.2 * t + k));
      const v = s * env * gain;
      add(i, v * (0.6 - pan * 0.5), v * (0.6 + pan * 0.5));
    }
  }
}
// ---------- pluck ----------
function pluck(t, m, gain, pan = 0) {
  const f = mtof(m),
    i0 = Math.floor(t * SR),
    len = Math.floor(0.9 * SR);
  for (let j = 0; j < len; j++) {
    const tt = j / SR,
      env = Math.exp(-tt * 6) * Math.min(1, tt / 0.004);
    const s = Math.sin(
      2 * Math.PI * f * tt + 0.8 * Math.sin(2 * Math.PI * f * 2 * tt) * Math.exp(-tt * 10),
    );
    add(i0 + j, s * env * gain * (1 - pan), s * env * gain * (1 + pan));
  }
}
// ---------- bell (signature) ----------
function bell(t, m, gain, pan = 0, decay = 2.2) {
  const f = mtof(m),
    i0 = Math.floor(t * SR),
    len = Math.floor(decay * 2 * SR);
  for (let j = 0; j < len; j++) {
    const tt = j / SR,
      env = Math.exp(-tt * (3 / decay)) * Math.min(1, tt / 0.003);
    const s =
      Math.sin(
        2 * Math.PI * f * tt + 1.4 * Math.exp(-tt * 2) * Math.sin(2 * Math.PI * f * 3.5 * tt),
      ) +
      0.3 * Math.sin(2 * Math.PI * f * 2 * tt) * Math.exp(-tt * 4);
    add(i0 + j, s * env * gain * (1 - pan), s * env * gain * (1 + pan));
  }
}
function boom(t, gain) {
  const i0 = Math.floor(t * SR);
  for (let j = 0; j < 1.6 * SR; j++) {
    const tt = j / SR;
    const f = 40 + 60 * Math.exp(-tt * 18);
    add(i0 + j, Math.sin(2 * Math.PI * f * tt) * Math.exp(-tt * 2.2) * gain);
  }
}
function kick(t, gain) {
  const i0 = Math.floor(t * SR);
  let ph = 0;
  for (let j = 0; j < 0.35 * SR; j++) {
    const tt = j / SR;
    ph += (2 * Math.PI * (48 + 110 * Math.exp(-tt * 30))) / SR;
    add(i0 + j, Math.sin(ph) * Math.exp(-tt * 9) * gain);
  }
}
function hat(t, gain) {
  const i0 = Math.floor(t * SR);
  let lp = 0;
  for (let j = 0; j < 0.06 * SR; j++) {
    const n = rnd();
    const hp = n - lp;
    lp = n * 0.3 + lp * 0.7;
    const e = Math.exp(-(j / SR) * 70) * gain;
    add(i0 + j, hp * e * 0.8, hp * e);
  }
}
function noiseSweep(t, dur, gain, up = true) {
  const i0 = Math.floor(t * SR),
    len = Math.floor(dur * SR);
  let y = 0;
  for (let j = 0; j < len; j++) {
    const x = j / len,
      cut = up ? 0.02 + 0.35 * x : 0.37 - 0.35 * x;
    y += cut * (rnd() - y);
    const e = Math.sin(Math.PI * x) ** 2 * gain;
    add(i0 + j, y * e * (1 - x * 0.6), y * e * (0.4 + x * 0.6));
  }
}
function blip(t, f0, f1, dur, gain) {
  const i0 = Math.floor(t * SR),
    len = Math.floor(dur * SR);
  let ph = 0;
  for (let j = 0; j < len; j++) {
    const x = j / len;
    ph += (2 * Math.PI * (f0 + (f1 - f0) * x)) / SR;
    add(i0 + j, Math.sin(ph) * Math.exp(-x * 4) * Math.min(1, j / 40) * gain);
  }
}
function tick(t, gain) {
  // UI tap: soft click
  blip(t, 1400, 900, 0.035, gain);
  const i0 = Math.floor(t * SR);
  for (let j = 0; j < 0.006 * SR; j++) add(i0 + j, rnd() * gain * 0.25 * (1 - j / (0.006 * SR)));
}

// ---------- arrangement ----------
// intro signature: low boom + rising bell motif C E G C, then resolve
boom(0.35, 0.55);
noiseSweep(0.0, 0.6, 0.12);
[
  [72, 0.45],
  [76, 0.62],
  [79, 0.79],
  [84, 1.05],
].forEach(([m, t], k) => bell(t, m, 0.16, -0.3 + k * 0.2));
bell(1.05, 60, 0.12, 0, 3);
pad(0.4, introEnd, [48, 55, 64, 67], 0.022);

// main bed
let ci = 0;
for (let t = introEnd; t < outroAt; t += bar, ci++) {
  const ch = chords[ci % 4];
  pad(t, Math.min(t + bar, outroAt), ch, 0.018);
  const arp = [
    ch[0] + 24,
    ch[2] + 12,
    ch[3] + 12,
    ch[4] + 12,
    ch[1] + 24,
    ch[3] + 12,
    ch[4] + 12,
    ch[2] + 24,
  ];
  for (let s = 0; s < 8; s++) {
    const tt = t + (s * beat) / 2;
    if (tt >= outroAt) break;
    pluck(tt, arp[s], 0.05 + (s % 2 ? 0 : 0.015), s % 2 ? 0.3 : -0.3);
  }
  for (let b = 0; b < 4; b++) {
    const tt = t + b * beat;
    if (tt >= outroAt) break;
    if (ci > 0 && b % 2 === 0) kick(tt, 0.32);
    if (ci > 0) hat(tt + beat / 2, 0.11);
  }
  pluck(t, ch[0] + 12, 0.07); // bass note
}

// outro: same signature, resolving and longer
noiseSweep(outroAt - 0.4, 0.8, 0.12);
boom(outroAt + 0.1, 0.5);
[
  [84, 0.2],
  [79, 0.38],
  [76, 0.56],
  [72, 0.8],
  [79, 1.2],
  [84, 1.5],
].forEach(([m, t], k) => bell(outroAt + t, m, 0.13, 0.3 - k * 0.12, 3));
pad(outroAt, end + 0.3, [48, 55, 59, 64, 67], 0.026);

// UI sounds
for (const c of cues) {
  if (c.type === "tap") tick(c.t, 0.22);
  if (c.type === "key") blip(c.t, 2400 + rnd() * 300, 2000, 0.012, 0.035);
  if (c.type === "whoosh") noiseSweep(c.t - 0.25, 0.55, 0.16);
  if (c.type === "send") {
    noiseSweep(c.t, 0.35, 0.1);
    blip(c.t + 0.12, 700, 1500, 0.12, 0.12);
  }
  if (c.type === "notify") {
    bell(c.t, 88, 0.1, -0.2, 0.9);
    bell(c.t + 0.14, 95, 0.09, 0.2, 1.1);
  }
  if (c.type === "lost") {
    bell(c.t, 64, 0.1, -0.2, 1.4);
    bell(c.t + 0.18, 60, 0.1, 0.2, 1.8);
  }
  if (c.type === "success")
    [76, 79, 84, 88].forEach((m, k) => bell(c.t + k * 0.07, m, 0.08, -0.3 + k * 0.2, 1.4));
}

// ---------- space: stereo feedback delay ----------
const d = Math.floor(beat * 0.75 * SR),
  fb = 0.28,
  mix = 0.22;
for (let i = d; i < N; i++) {
  L[i] += R[i - d] * fb * mix;
  R[i] += L[i - d] * fb * mix;
}
// fade out and normalise
const fo = Math.floor(1.5 * SR);
for (let j = 0; j < fo; j++) {
  const g = 1 - j / fo;
  L[N - fo + j] *= g;
  R[N - fo + j] *= g;
}
let peak = 0;
for (let i = 0; i < N; i++) peak = Math.max(peak, Math.abs(L[i]), Math.abs(R[i]));
const g = 0.89 / peak;
const buf = Buffer.alloc(44 + N * 4);
buf.write("RIFF", 0);
buf.writeUInt32LE(36 + N * 4, 4);
buf.write("WAVEfmt ", 8);
buf.writeUInt32LE(16, 16);
buf.writeUInt16LE(1, 20);
buf.writeUInt16LE(2, 22);
buf.writeUInt32LE(SR, 24);
buf.writeUInt32LE(SR * 4, 28);
buf.writeUInt16LE(4, 32);
buf.writeUInt16LE(16, 34);
buf.write("data", 36);
buf.writeUInt32LE(N * 4, 40);
for (let i = 0; i < N; i++) {
  buf.writeInt16LE(Math.round(Math.tanh(L[i] * g * 1.1) * 32000), 44 + i * 4);
  buf.writeInt16LE(Math.round(Math.tanh(R[i] * g * 1.1) * 32000), 46 + i * 4);
}
fs.writeFileSync(process.argv[3] || "soundtrack.wav", buf);
console.log("soundtrack", DUR.toFixed(1), "s, peak", peak.toFixed(2));
