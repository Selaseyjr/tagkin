// Records a Tagkin video by driving the real prototypes inside stage.html.
// Usage: node rec.mjs owner|finder  → frames_<name>/ + timeline_<name>.json
import { chromium } from "playwright";
import fs from "node:fs";

const NAME = process.argv[2];
const dir = process.cwd();
const fdir = `${dir}/frames_${NAME}`;
fs.rmSync(fdir, { recursive: true, force: true });
fs.mkdirSync(fdir);

const browser = await chromium.launch();
const page = await browser.newPage({
  viewport: { width: 1920, height: 1080 },
  deviceScaleFactor: 1,
});
await page.goto(`file://${dir}/stage.html`);
await page.evaluate(() => document.fonts.ready);
await page.waitForTimeout(1500);
const css = `.ctl,.proto-l,.proto,#toast{display:none!important}
html,body{margin:0!important;padding:0!important;overflow:hidden!important}
body>*{max-width:none!important}
.stage{max-width:none!important;width:390px!important;margin:0!important}
.stage .scr{border:0!important;border-radius:0!important;min-height:844px!important;height:844px!important;padding-top:56px!important;box-shadow:none!important}
.sbar{display:none!important}`;
const frame = (n) => page.frame({ url: new RegExp(n + "-prototype") });
for (const n of ["finder", "owner"]) await frame(n).addStyleTag({ content: css });

const cdp = await page.context().newCDPSession(page);
const frames = [];
cdp.on("Page.screencastFrame", async ({ data, metadata, sessionId }) => {
  const file = `frames_${NAME}/${String(frames.length).padStart(5, "0")}.jpg`;
  fs.writeFileSync(`${dir}/${file}`, Buffer.from(data, "base64"));
  frames.push({ file, wall: metadata.timestamp });
  await cdp.send("Page.screencastFrameAck", { sessionId }).catch(() => {});
});
const cues = [];
const cue = (type) => cues.push({ type, wall: Date.now() / 1000 });
const wait = (ms) => page.waitForTimeout(ms);

await page.evaluate(() => scene(""));
await cdp.send("Page.startScreencast", {
  format: "jpeg",
  quality: 92,
  maxWidth: 1920,
  maxHeight: 1080,
  everyNthFrame: 1,
});
await wait(300);
const keepAlive = setInterval(
  () =>
    page
      .evaluate(() => {
        document.body.style.outline = document.body.style.outline ? "" : "0px solid transparent";
      })
      .catch(() => {}),
  33,
);

let TOTAL = 7;
const cap = (k, h, p, s) =>
  page.evaluate(([k, h, p, s, T]) => caption(k, h, p, s, T), [k, h, p, s, TOTAL]);
const app = (id) => page.evaluate((id) => app(id), id);
const show = (n, id) => frame(n).evaluate((id) => show(id), id);
const loc = (n, sel) =>
  typeof sel === "string" ? frame(n).locator(`.stage .scr.on ${sel}`).first() : sel;
const text = (n, t, sel = "*") =>
  frame(n).locator(`.stage .scr.on ${sel}`).filter({ hasText: t }).last();
const tap = async (n, sel, after = 0) => {
  const l = loc(n, sel);
  await l.scrollIntoViewIfNeeded().catch(() => {});
  const [x, y] = await l.evaluate((e) => {
    const r = e.getBoundingClientRect();
    return [r.x + r.width / 2, r.y + r.height / 2];
  });
  await page.evaluate(([x, y]) => tapAt(x, y), [x, y]);
  cue("tap");
  await wait(220);
  await l.evaluate((e) => {
    e.focus?.();
    e.click();
  });
  if (after) await wait(after);
};
const type = async (n, sel, s, clear = true) => {
  const l = loc(n, sel);
  await tap(n, l);
  if (clear)
    await l.evaluate((e) => {
      e.value = "";
      e.dispatchEvent(new Event("input", { bubbles: true }));
    });
  for (const ch of s) {
    await l.evaluate((e, ch) => {
      e.value += ch;
      e.dispatchEvent(new Event("input", { bubbles: true }));
    }, ch);
    cue("key");
    await wait(50 + Math.random() * 40);
  }
};
const intro = async (title) => {
  await page.evaluate((t) => setTitle(t), title);
  await page.evaluate(() => scene("intro"));
  cue("intro");
  await wait(5200);
};
const outro = async () => {
  await page.evaluate(() => scene("outro"));
  cue("outro");
  await wait(7500);
};
const main = async () => {
  await page.evaluate(() => scene("main"));
  cue("whoosh");
};

// ===================== OWNER =====================
async function owner() {
  TOTAL = 7;
  await show("owner", "launch1");
  await app("owner");
  await intro("Owner experience");
  await main();
  await cap(
    "Welcome",
    "Protect what you value.",
    "Tag your bags, keys, gear and pets. If one goes missing, the finder can alert you.",
    1,
  );
  await wait(3800);
  await tap("owner", text("owner", "Next", ".btn"), 1400);
  await tap("owner", text("owner", "Start exploring", ".btn"), 1200);

  await cap(
    "Create a tag",
    "Add a tag in a few steps.",
    "Choose a style, name the item and write what the finder reads.",
    2,
  );
  await wait(1300);
  await tap("owner", text("owner", "For myself", ".btn"), 1200);
  await tap("owner", text("owner", "Sticker", ".gcard"), 1200);
  await tap("owner", text("owner", "Next", ".btn"), 1000);
  await type("owner", "#it-name", "Black backpack");
  await wait(500);
  await tap("owner", text("owner", "Next", ".btn"), 1200);
  await wait(1200);
  await tap("owner", text("owner", "Use this message", ".btn"), 1200);

  await cap(
    "Design",
    "Make it yours.",
    "Pick a colour, size and finish, with a live preview of the printed tag.",
    3,
  );
  await wait(800);
  const sw = frame("owner").locator(".stage .scr.on .swc");
  await tap("owner", sw.nth(3), 900);
  await tap("owner", sw.nth(5), 900);
  await tap("owner", text("owner", "Gloss", ".chip"), 900);
  await type("owner", "#cz-label", "K.B.");
  await wait(1300);
  await tap("owner", text("owner", "Continue to order", ".btn"), 1300);

  await cap(
    "Order",
    "Printed and delivered.",
    "Sign in with an email code, no password. Then a clear total and checkout.",
    4,
  );
  await wait(2000);
  await tap("owner", text("owner", "Continue to payment", ".btn"), 1200);
  await type("owner", "input", "alex@example.com");
  await wait(400);
  await tap("owner", text("owner", "Send code", ".btn"), 0);
  cue("notify");
  await wait(2200);
  await tap("owner", text("owner", "Continue", ".btn"), 2600);
  await tap("owner", ".paybtn", 0);
  cue("success");
  await wait(2600);
  await tap("owner", text("owner", "Continue", ".btn"), 1300);
  await tap("owner", text("owner", "Turn on notifications", ".btn"), 2600);

  await cap(
    "Lost mode",
    "Mark it as lost.",
    "The finder sees it is missing, and every scan shows you where it was seen.",
    5,
  );
  await wait(800);
  await tap("owner", text("owner", "Black backpack", ".item"), 1800);
  await tap("owner", text("owner", "Mark as lost", ".btn"), 1400);
  await tap("owner", text("owner", "Mark as lost", ".btn"), 0);
  cue("lost");
  await wait(3600);

  await cap(
    "Settings",
    "Your app, your way.",
    "Notifications, language, privacy and a light or dark look.",
    6,
  );
  await show("owner", "tags");
  await wait(1600);
  await tap("owner", '.tab[data-go="account"]', 1800);
  await tap("owner", text("owner", "Notifications", ".li"), 1400);
  await tap("owner", frame("owner").locator(".stage .scr.on .sw").last(), 1000);
  await tap("owner", ".back", 1000);
  await tap("owner", text("owner", "Appearance", ".li"), 1200);
  await tap("owner", '[data-theme-set="dark"]', 1600);
  await tap("owner", ".back", 1300);
  await tap("owner", '.tab[data-go="tags"]', 2400);
  await show("owner", "appearance");
  await wait(500);
  await tap("owner", '[data-theme-set="light"]', 1500);

  await cap(
    "Found",
    "Know when it’s found.",
    "A finder reports it. You read where it is and reply, privately.",
    7,
  );
  await wait(500);
  await show("owner", "alert");
  cue("notify");
  await wait(3600);
  await tap("owner", text("owner", "Open message", ".btn"), 3800);
  await outro();
}

// ===================== FINDER =====================
async function finder() {
  TOTAL = 6;
  await frame("finder").evaluate(() => scan("lost"));
  await app("finder");
  await page.evaluate(() => cam("on"));
  await intro("Finder experience");
  await main();
  await cap(
    "Scan",
    "Found something with a tag?",
    "Scan it with any phone camera. No app, no sign-up.",
    1,
  );
  await wait(3200);
  await page.evaluate(() => cam("hit"));
  cue("notify");
  await wait(900);
  await page.evaluate(() => cam("off"));
  cue("whoosh");
  await wait(1200);
  await cap(
    "The owner’s message",
    "See who it belongs to.",
    "The owner’s message, in your language where supported, with a photo of the item.",
    2,
  );
  await wait(3600);
  for (const v of ["pet", "travel"]) {
    await frame("finder").evaluate((v) => scan(v), v);
    cue("whoosh");
    await wait(2300);
  }
  await frame("finder").evaluate(() => scan("lost"));
  cue("whoosh");
  await wait(1600);

  await cap(
    "Report",
    "Say where it is.",
    "Three short steps: where it is now, the exact place and an optional note.",
    3,
  );
  await tap("finder", "#f-found", 1100);
  await tap("finder", text("finder", "With me", ".opt"), 700);
  await tap("finder", "#f-wherenext", 1000);
  await type("finder", "#f-placein", "Darmstadt Hbf, platform 4");
  await wait(500);
  await tap("finder", "#f-placenext", 1000);
  await type("finder", "#f-notein", "At the café by the stairs");
  await wait(400);
  await tap("finder", "#f-notenext", 1000);

  await cap(
    "Private by default",
    "Your details stay hidden.",
    "Add an email for replies, or stay anonymous. The owner never sees it.",
    4,
  );
  await wait(800);
  await type("finder", "#f-mail", "mia@example.com");
  await wait(400);
  await tap("finder", "#f-send", 0);
  cue("send");
  await wait(2600);

  await cap(
    "Chat",
    "Talk to the owner.",
    "Messages are relayed by Tagkin, so neither side shares a number.",
    5,
  );
  await wait(2600);
  await type("finder", "#f-rmsg", "I’ll wait at the café.");
  await wait(300);
  await tap("finder", "#f-sendbtn", 0);
  cue("send");
  await wait(2400);

  await cap(
    "Handover",
    "Hand it back safely.",
    "The owner shows a code. A match means it goes to the right person.",
    6,
  );
  await tap("finder", text("finder", "Handing it over", ".link"), 1200);
  await type("finder", "#f-hcode", "739204");
  await wait(400);
  await tap("finder", "#f-hcheck", 0);
  cue("success");
  await wait(1800);
  const done = text("finder", "handed it over", ".btn");
  if (await done.count()) await tap("finder", done, 2600);
  await wait(1200);
  await outro();
}

await (NAME === "owner" ? owner() : finder());

clearInterval(keepAlive);
await cdp.send("Page.stopScreencast");
await wait(300);
await browser.close();
const base = frames[0].wall;
const end = Date.now() / 1000 - base;
fs.writeFileSync(
  `${dir}/timeline_${NAME}.json`,
  JSON.stringify(
    {
      frames: frames.map((f) => ({ file: f.file, t: f.wall - base })),
      cues: cues.map((c) => ({ type: c.type, t: c.wall - base })),
      end,
    },
    null,
    1,
  ),
);
console.log(NAME, "frames", frames.length, "end", end.toFixed(1));
