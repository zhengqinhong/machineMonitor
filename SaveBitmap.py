class SaveBitmap:
    def __init__(self, w=1920, h=1080):
        self.m_w = w
        self.m_h = h
        self.dataSize = 0
        self.bmp_header = [0x42, 0x4d]

    def init(self, w, h):
        self.m_w = w
        self.m_h = h

    def conv2byte(self, l, num, len):
        tmp = num
        for i in range(len):
            l.append(tmp & 0x000000ff)
            tmp >>= 8

    def calc_data_size(self):
        if ((self.m_w * 3) % 4 == 0):
            self.dataSize = self.m_w * 3 * self.m_h
        else:
            self.dataSize = (((self.m_w * 3) // 4 + 1) * 4) * self.m_h
        # self.dataSize = self.m_w * self.m_h * 3
        self.fileSize = self.dataSize + 54

    def gen_bmp_header(self):
        self.calc_data_size()
        self.bmp_header = [0x42, 0x4d]
        self.conv2byte(self.bmp_header, self.fileSize, 4)  # file size
        self.conv2byte(self.bmp_header, 0, 2)
        self.conv2byte(self.bmp_header, 0, 2)
        self.conv2byte(self.bmp_header, 54, 4)  # rgb data offset
        self.conv2byte(self.bmp_header, 40, 4)  # info block size
        self.conv2byte(self.bmp_header, self.m_w, 4)
        self.conv2byte(self.bmp_header, -self.m_h, 4)   #正-倒立  负-正立
        self.conv2byte(self.bmp_header, 1, 2)
        self.conv2byte(self.bmp_header, 24, 2)  # 888
        self.conv2byte(self.bmp_header, 0, 4)  # no compression
        self.conv2byte(self.bmp_header, self.dataSize, 4)  # rgb data size
        self.conv2byte(self.bmp_header, 0, 4)
        self.conv2byte(self.bmp_header, 0, 4)
        self.conv2byte(self.bmp_header, 0, 4)
        self.conv2byte(self.bmp_header, 0, 4)

    def save(self, byte, dir):
    #    print(t_filename)
        self.gen_bmp_header()
        fh = open(dir, 'wb')
        fh.write(bytes(self.bmp_header))
        fh.write(byte)
        fh.close()
        return True

    def set_width(self, w):
        self.m_w = w

    def set_height(self, h):
        self.m_h = h
