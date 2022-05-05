    def get_section_sets(self):
        # First check if the URL list file exists
        fname = self.url_file
        if not URLMaker.check_file_exists(fname):
            print("Error, file not found:", fname)
            return

        url_pattern = re.compile(r'data-url="(.*)"')
        title_pattern = re.compile(r'title="(.*)"')
        img_pattern = re.compile(r'image="(.*)"')

        section_dict = dict()
        section_dict['__NOSECTION__'] = []

        line_cnt = 0
        f = open(fname, 'r', encoding='utf-8')

        cur_sect_name = '__NOSECTION__'
        for line in f.readlines():
            line_cnt += 1
            l = line.strip()
            if len(l) == 0:
                continue
            if l.startswith("<!--"):
                llist = l.split()
                if len(llist) == 3:
                    cur_sect_name = llist[1]
                    section_dict[cur_sect_name] = []
                continue
            if not l.startswith("data-url"):
                continue

            kwlist = l.split(",")
            assert len(kwlist) == 2 or len(kwlist) == 3

            url_m = url_pattern.match(kwlist[0].strip())
            title_m = title_pattern.match(kwlist[1].strip())
            img_m = img_pattern.match(kwlist[2].strip()) if len(kwlist) == 3 else None

            if url_m is None or title_m is None:
                continue
            str_url = url_m.group(1)
            str_webname = title_m.group(1)
            str_imgf = "undef128x128.png" if img_m is None else img_m.group(1)
            str_imgf = "undef128x128.png" if len(str_imgf) == 0 else str_imgf
            str_descri = str_webname

            csect = section_dict[cur_sect_name]
            csect.append([str_url, str_webname, str_imgf, str_descri])

        f.close()

        for sname, msglist in section_dict.items():
            print("Section {} has {} items".format(sname, len(msglist)))
            for urlstr in msglist:
                print("\t", urlstr)
