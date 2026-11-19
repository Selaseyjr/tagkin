#!/usr/bin/env bash
# make.sh <name> : record, score and encode one video, plus a contact sheet
set -euo pipefail
n=$1; FF=node_modules/ffmpeg-static/ffmpeg
[ "${SKIP_REC:-}" ] || node rec.mjs $n
node music.mjs timeline_$n.json sound_$n.wav
python3 - $n <<'PY'
import json,sys
n=sys.argv[1];d=json.load(open(f'timeline_{n}.json'));fr=d['frames'];o=[]
for i,f in enumerate(fr):
    nx=fr[i+1]['t'] if i+1<len(fr) else d['end']
    o.append(f"file '{f['file']}'\nduration {max(nx-f['t'],0.001):.4f}")
o.append(f"file '{fr[-1]['file']}'");open(f'frames_{n}.txt','w').write('\n'.join(o))
PY
[ "${SKIP_ENC:-}" ] || $FF -y -loglevel error -f concat -safe 0 -i frames_$n.txt -i sound_$n.wav -vf "scale=1920:1080,fps=30,format=yuv420p" -c:v libx264 -preset slow -crf 17 -profile:v high -af "loudnorm=I=-16:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k -movflags +faststart -shortest tagkin-$n.mp4
dur=$( ($FF -i tagkin-$n.mp4 2>&1 || true) | grep -o "Duration: [0-9:.]*" | cut -d' ' -f2)
echo "$n $dur"
args=(); filt=""; k=0
for p in 0.08 0.17 0.25 0.33 0.42 0.5 0.58 0.67 0.75 0.83 0.9 0.97; do
  s=$(python3 -c "h,m,x='$dur'.split(':');print(round((int(h)*3600+int(m)*60+float(x))*$p,1))")
  $FF -y -loglevel error -ss $s -i tagkin-$n.mp4 -frames:v 1 -vf scale=640:-1 s_${n}_$k.jpg; args+=(-i s_${n}_$k.jpg); k=$((k+1))
done
$FF -y -loglevel error "${args[@]}" -filter_complex "[0][1][2][3]hstack=4[a];[4][5][6][7]hstack=4[b];[8][9][10][11]hstack=4[c];[a][b][c]vstack=3" sheet_$n.jpg
