"""Build branded before/after images for Perfect Panes posts.
Usage: python3 brand/make_post.py <before.jpg> <after.jpg> "<Service · Town>" <out-base> [bx,by ax,ay]
Writes <out-base>-tall.jpg (Instagram 4:5) and <out-base>-wide.jpg (Google)."""
import sys, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps
HERE=os.path.dirname(os.path.abspath(__file__))
B='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'; R='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
NAVY=(12,30,55)
def logo():
    lg=Image.open(os.path.join(HERE,'logo-orange.png')).convert('RGB')
    orange=lg.getpixel((5,5))
    arr=np.asarray(lg).astype(float); o=np.array(orange,float)
    a=np.clip(np.linalg.norm(arr-o,axis=2)/np.linalg.norm(np.array([255,255,255.])-o),0,1)
    w=Image.new('RGBA',lg.size,(255,255,255,0)); w.putalpha(Image.fromarray((a*255).astype('uint8')))
    return w, orange
def pill(d,txt,x,y,col,size):
    f=ImageFont.truetype(B,size); tw=d.textlength(txt,font=f); h=int(size*1.7)
    d.rounded_rectangle([x,y,x+tw+int(size*0.96),y+h],radius=h//2,fill=col,outline='white',width=4); d.text((x+int(size*0.48),y+int(size*0.28)),txt,font=f,fill='white')
def strip(t,d,line,W,H,bar,white):
    y0=H-bar; lh=int(bar*0.80); lw=int(white.width*lh/white.height)
    L=white.resize((lw,lh),Image.LANCZOS); t.paste(L,(48,y0+(bar-lh)//2),L)
    size=int(bar*0.26); avail=W-48-lw-40-60
    while size>18 and d.textlength(line,font=ImageFont.truetype(B,size))>avail: size-=1
    fs=ImageFont.truetype(B,size); f3=ImageFont.truetype(R,int(bar*0.20))
    s='★★★★★  5.0 on Google'
    d.text((W-60-d.textlength(line,font=fs),y0+int(bar*0.22)),line,font=fs,fill='white')
    d.text((W-60-d.textlength(s,font=f3),y0+int(bar*0.58)),s,font=f3,fill='white')

def strip_big(t,d,service,town,W,H,bar,white):
    """Taller strip for the 4:5 Instagram image: service line large across the top, logo and town underneath."""
    y0=H-bar; pad=54
    size=66
    while size>30 and d.textlength(service,font=ImageFont.truetype(B,size))>W-2*pad: size-=1
    fs=ImageFont.truetype(B,size)
    d.text((pad,y0+22+(66-size)//2),service,font=fs,fill='white')
    lh=96; lw=int(white.width*lh/white.height); ly=y0+bar-lh-22
    L=white.resize((lw,lh),Image.LANCZOS); t.paste(L,(pad-6,ly),L)
    f3=ImageFont.truetype(B,40); f4=ImageFont.truetype(R,34)
    d.text((W-pad-d.textlength(town,font=f3),ly+2),town,font=f3,fill='white')
    s2='★★★★★  5.0 on Google'
    d.text((W-pad-d.textlength(s2,font=f4),ly+52),s2,font=f4,fill='white')
def build(before,after,line,out,cb=(0.5,0.3),ca=(0.5,0.4)):
    white,ORANGE=logo()
    b=ImageOps.exif_transpose(Image.open(before)).convert('RGB'); a=ImageOps.exif_transpose(Image.open(after)).convert('RGB')
    # tall 4:5
    W,H,bar,g=1080,1350,236,8; ph=(H-bar-g)//2
    t=Image.new('RGB',(W,H),ORANGE)
    t.paste(ImageOps.fit(b,(W,ph),Image.LANCZOS,centering=cb),(0,0)); t.paste(ImageOps.fit(a,(W,ph),Image.LANCZOS,centering=ca),(0,ph+g))
    d=ImageDraw.Draw(t); pill(d,'BEFORE',60,34,NAVY,46); pill(d,'AFTER',60,ph+g+34,ORANGE,46); sv,tn=[x.strip() for x in line.split('·')]; strip_big(t,d,sv,tn,W,H,bar,white)
    t.save(out+'-tall.jpg',quality=90)
    # wide for Google
    W,H,bar,g=2000,1280,170,10; pw=(W-g)//2; phh=H-bar
    w=Image.new('RGB',(W,H),ORANGE)
    w.paste(ImageOps.fit(b,(pw,phh),Image.LANCZOS,centering=cb),(0,0)); w.paste(ImageOps.fit(a,(pw,phh),Image.LANCZOS,centering=ca),(pw+g,0))
    d=ImageDraw.Draw(w); pill(d,'BEFORE',50,40,NAVY,56); pill(d,'AFTER',pw+g+50,40,ORANGE,56); strip(w,d,line,W,H,bar,white)
    w.save(out+'-wide.jpg',quality=90)
if __name__=='__main__':
    a=sys.argv; c=[tuple(float(x) for x in p.split(',')) for p in a[5:7]] if len(a)>6 else [(0.5,0.3),(0.5,0.4)]
    build(a[1],a[2],a[3],a[4],c[0],c[1])
