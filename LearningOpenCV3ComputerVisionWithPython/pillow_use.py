# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import numpy as np
from IPython.display import display


class ChannelFilter(object):
    
    def __init__(self, img_path):
        self.img = Image.open('aqi.png')
        self.img = self.img.convert('RGB')
        self.fnt = ImageFont.truetype("F:/Documents/google_fonts/times.ttf",
                                      size=40)
        self.raw_img = Image.new(self.img.mode, 
                            (self.img.width * 3, self.img.height * 3 + 200))

    def make_trans(self, img_obj, channel, rate):
        tmp_array = []
        for y in range(img_obj.height):
            line_array = []
            for x in range(img_obj.width):
                r, g, b = img_obj.getpixel((x, y))
                if channel == 'R':
                    r *= rate
                elif channel == 'G':
                    g *= rate
                elif channel == 'B':
                    b *= rate
                line_array.append((r, g, b))
            tmp_array.append(line_array)
        else:
            new_img = Image.fromarray(np.asarray(tmp_array, dtype=np.uint8))
            return new_img
    
    
    def combine2one(self, img_list):
        # 把 9 张图片放在一起
        # 3x3 布局
        
        x = y = 0
        rate_list = [0.1, 0.5, 0.9]
        text_str = "channel {idx} intensity {rate}"
        for idx, im in enumerate(img_list):
            if idx >= 3 and idx % 3 == 0:
                y += 60
            text = text_str.format(idx=int(idx/3), rate=rate_list[idx%3])
            self.draw_text(text, x, y + self.img.height)
            self.raw_img.paste(im, (x, y))
            if x + self.img.width == self.raw_img.width:
                y += self.img.height
                x = 0
            else:
                x += self.img.width
        else:
            self.raw_img = self.raw_img.resize((int(self.raw_img.width / 2), 
                                                int(self.raw_img.height / 2)))
    
    def draw_text(self, text, x, y):
        
        
        draw_img = ImageDraw.Draw(self.raw_img)
        draw_img.text((x, y), 
                      text=text, 
                      font=self.fnt,
                      fill='white')
    
    
    def main(self):
        # main processing
        total_img = []
        for chan in ['R', 'G', 'B']:
            for rate in [0.1, 0.5, 0.9]:
                tmp_img = self.make_trans(self.img, chan, rate)
                total_img.append(tmp_img)
        self.combine2one(total_img)
        self.raw_img.save('combined.png')
        

if __name__ == '__main__':
    
    img = 'aqi.png'
    cf = ChannelFilter(img)
    cf.main()
    