import json, subprocess
FF = 'node_modules/ffmpeg-static/ffmpeg'
src = {'walk': ('tagkin-walkthrough.mp4', 'timeline.json'), 'finder': ('tagkin-finder.mp4', 'timeline_finder.json'), 'owner': ('tagkin-owner.mp4', 'timeline_owner.json')}
segs = [('walk', 0.0, 4.8), ('finder', 6.0, 4.2), ('finder', 20.4, 4.6), ('owner', 25.4, 4.0), ('owner', 53.5, 4.0), ('owner', 67.0, 4.0), ('owner', 76.0, 4.0), ('walk', 53.7, 6.0)]
X = 0.35
inputs, filt, cues, off = [], [], [], 0.0
for i, (k, s, d) in enumerate(segs):
    inputs += ['-ss', str(s), '-t', str(d), '-i', src[k][0]]
    filt.append(f'[{i}:v]settb=AVTB,setpts=PTS-STARTPTS,fps=30[v{i}]')
    tl = json.load(open(src[k][1]))
    for c in tl['cues']:
        if s <= c['t'] < s + d and c['type'] not in ('intro', 'outro'):
            cues.append({'type': c['type'], 't': off + c['t'] - s})
    if i == 0: cues.append({'type': 'intro', 't': 0.3})
    elif i == len(segs) - 1: cues.append({'type': 'outro', 't': off + 0.2})
    else: cues.append({'type': 'whoosh', 't': off + 0.1})
    seg_off = off
    off += d - X
end = off + X
prev, acc = 'v0', segs[0][2]
for i in range(1, len(segs)):
    o = acc - X
    filt.append(f'[{prev}][v{i}]xfade=transition=fade:duration={X}:offset={o:.3f}[x{i}]')
    prev, acc = f'x{i}', acc + segs[i][2] - X
json.dump({'cues': sorted(cues, key=lambda c: c['t']), 'end': end}, open('timeline_teaser.json', 'w'))
subprocess.run([FF, '-y', '-loglevel', 'error', *inputs, '-filter_complex', ';'.join(filt), '-map', f'[{prev}]', '-an', '-c:v', 'libx264', '-preset', 'slow', '-crf', '17', '-pix_fmt', 'yuv420p', 'teaser_v.mp4'], check=True)
print('teaser', round(end, 1), 's', len(cues), 'cues')
