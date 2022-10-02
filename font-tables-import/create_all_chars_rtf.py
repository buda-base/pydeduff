def create_rtf(font_list, fname):
	with open(fname, "wb") as f:
		f.write(b"{\\rtf1\\ansi \\deff69\\deflang1033 {\\fonttbl{\\f2\\fnil\\fcharset2\\fprq2 Some font;}")
		fontidx = 100
		fontname_to_font_idx = {}
		for fontname, fontinfo in font_list.items():
			f.write(("{\\f%d\\fnil\\fcharset2\\fprq2 %s;}" % (fontidx, fontname)).encode("utf-8"))
			fontname_to_font_idx[fontname] = fontidx
			fontidx += 1
		f.write(b"}\n")
		for fontname, fontinfo in font_list.items():
			fontidx = fontname_to_font_idx[fontname]
			for i in range(32, fontinfo["maxc"]+1):
				s = "\\f2\\fs48%s,%d,\\f%d\\fs48\\'%x\\par\n" % (fontname, i, fontidx, i)
				f.write(s.encode("utf-8"))
		f.write(b"}")

font_list_attu = {
	"Ededris-syma": {"maxc": 127},
	"Ededris-vowa": {"maxc": 127},
	"Ededris-a": {"maxc": 127},
	"Ededris-a1": {"maxc": 127},
	"Ededris-a2": {"maxc": 127},
	"Ededris-a3": {"maxc": 127},
	"Ededris-b": {"maxc": 127},
	"Ededris-b1": {"maxc": 127},
	"Ededris-b2": {"maxc": 127},
	"Ededris-b3": {"maxc": 127},
	"Ededris-c": {"maxc": 127},
	"Ededris-c1": {"maxc": 127},
	"Ededris-c2": {"maxc": 127},
	"Ededris-c3": {"maxc": 127},
	"Ededris-d": {"maxc": 127},
	"Ededris-d1": {"maxc": 127},
	"Ededris-d2": {"maxc": 127},
	"Ededris-d3": {"maxc": 127},
	"Ededris-e": {"maxc": 127},
	"Ededris-e1": {"maxc": 127},
	"Ededris-e2": {"maxc": 127},
	"Ededris-e3": {"maxc": 127},
	"Ededris-f": {"maxc": 127},
	"Ededris-f1": {"maxc": 127},
	"Ededris-f2": {"maxc": 127},
	"Ededris-f3": {"maxc": 127},
	"Ededris-g": {"maxc": 127},
	"Ededris-g1": {"maxc": 127},
	"Ededris-g2": {"maxc": 127},
	"Ededris-g3": {"maxc": 127},
	"Dedris-syma": {"maxc": 127},
	"Dedris-vowa": {"maxc": 127},
	"Dedris-a": {"maxc": 127},
	"Dedris-a1": {"maxc": 127},
	"Dedris-a2": {"maxc": 127},
	"Dedris-a3": {"maxc": 127},
	"Dedris-b": {"maxc": 127},
	"Dedris-b1": {"maxc": 127},
	"Dedris-b2": {"maxc": 127},
	"Dedris-b3": {"maxc": 127},
	"Dedris-c": {"maxc": 127},
	"Dedris-c1": {"maxc": 127},
	"Dedris-c2": {"maxc": 127},
	"Dedris-c3": {"maxc": 127},
	"Dedris-d": {"maxc": 127},
	"Dedris-d1": {"maxc": 127},
	"Dedris-d2": {"maxc": 127},
	"Dedris-d3": {"maxc": 127},
	"Dedris-e": {"maxc": 127},
	"Dedris-e1": {"maxc": 127},
	"Dedris-e2": {"maxc": 127},
	"Dedris-e3": {"maxc": 127},
	"Dedris-f": {"maxc": 127},
	"Dedris-f1": {"maxc": 127},
	"Dedris-f2": {"maxc": 127},
	"Dedris-f3": {"maxc": 127},
	"Dedris-g": {"maxc": 127},
	"Dedris-g1": {"maxc": 127},
	"Dedris-g2": {"maxc": 127},
	"Dedris-g3": {"maxc": 127},
	"Drutsa-syma": {"maxc": 127},
	"Drutsa-vowa": {"maxc": 127},
	"Drutsa-a": {"maxc": 127},
	"Drutsa-a1": {"maxc": 127},
	"Drutsa-a2": {"maxc": 127},
	"Drutsa-a3": {"maxc": 127},
	"Drutsa-b": {"maxc": 127},
	"Drutsa-b1": {"maxc": 127},
	"Drutsa-b2": {"maxc": 127},
	"Drutsa-b3": {"maxc": 127},
	"Drutsa-c": {"maxc": 127},
	"Drutsa-c1": {"maxc": 127},
	"Drutsa-c2": {"maxc": 127},
	"Drutsa-c3": {"maxc": 127},
	"Drutsa-d": {"maxc": 127},
	"Drutsa-d1": {"maxc": 127},
	"Drutsa-d2": {"maxc": 127},
	"Drutsa-d3": {"maxc": 127},
	"Drutsa-e": {"maxc": 127},
	"Drutsa-e1": {"maxc": 127},
	"Drutsa-e2": {"maxc": 127},
	"Drutsa-e3": {"maxc": 127},
	"Drutsa-f": {"maxc": 127},
	"Drutsa-f1": {"maxc": 127},
	"Drutsa-f2": {"maxc": 127},
	"Drutsa-f3": {"maxc": 127},
	"Drutsa-g": {"maxc": 127},
	"Drutsa-g1": {"maxc": 127},
	"Drutsa-g2": {"maxc": 127},
	"Drutsa-g3": {"maxc": 127},
	"Khamdris-a": {"maxc": 127},
	"Khamdris-syma": {"maxc": 127},
	"Khamdris-vowa": {"maxc": 127},
	"Khamdris-a1": {"maxc": 127},
	"Khamdris-a2": {"maxc": 127},
	"Khamdris-a3": {"maxc": 127},
	"Khamdris-b": {"maxc": 127},
	"Khamdris-b1": {"maxc": 127},
	"Khamdris-b2": {"maxc": 127},
	"Khamdris-b3": {"maxc": 127},
	"Khamdris-c": {"maxc": 127},
	"Khamdris-c1": {"maxc": 127},
	"Khamdris-c2": {"maxc": 127},
	"Khamdris-c3": {"maxc": 127},
	"Khamdris-d": {"maxc": 127},
	"Khamdris-d1": {"maxc": 127},
	"Khamdris-d2": {"maxc": 127},
	"Khamdris-d3": {"maxc": 127},
	"Khamdris-e": {"maxc": 127},
	"Khamdris-e1": {"maxc": 127},
	"Khamdris-e2": {"maxc": 127},
	"Khamdris-e3": {"maxc": 127},
	"Khamdris-f": {"maxc": 127},
	"Khamdris-f1": {"maxc": 127},
	"Khamdris-f2": {"maxc": 127},
	"Khamdris-f3": {"maxc": 127},
	"Khamdris-g": {"maxc": 127},
	"Khamdris-g1": {"maxc": 127},
	"Khamdris-g2": {"maxc": 127},
	"Khamdris-g3": {"maxc": 127},
	"TCRC Bod-Yig": {"maxc": 255},
	"TCRC Youtso": {"maxc": 255},
	"TCRC Youtsoweb": {"maxc": 255},
	"TB-Youtso": {"maxc": 255},
	"TB-TTYoutso": {"maxc": 255},
	"Monlam ouchan 1": {"maxc": 255},
	"Monlam ouchan 2": {"maxc": 255},
	"Monlam ouchan 3": {"maxc": 255},
	"Monlam ouchan 4": {"maxc": 255},
	"Monlam yigchong": {"maxc": 255},
	"TB2-Youtso": {"maxc": 255},
	"TB2-TTYoutso": {"maxc": 255},
	"TibetanMachine": {"maxc": 255},
	"TibetanMachineSkt1": {"maxc": 255},
	"TibetanMachineSkt2": {"maxc": 255},
	"TibetanMachineSkt3": {"maxc": 255},
	"TibetanMachineSkt4": {"maxc": 255},
	"TibetanCalligraphic": {"maxc": 255},
	"TibetanCalligraphicSkt1": {"maxc": 255},
	"TibetanCalligraphicSkt2": {"maxc": 255},
	"TibetanCalligraphicSkt3": {"maxc": 255},
	"TibetanCalligraphicSkt4": {"maxc": 255},
	"TibetanChogyal": {"maxc": 255},
	"TibetanChogyalSkt1": {"maxc": 255},
	"TibetanChogyalSkt2": {"maxc": 255},
	"TibetanChogyalSkt3": {"maxc": 255},
	"TibetanChogyalSkt4": {"maxc": 255},
	"TibetanClassic": {"maxc": 255},
	"TibetanClassicSkt1": {"maxc": 255},
	"TibetanClassicSkt2": {"maxc": 255},
	"TibetanClassicSkt3": {"maxc": 255},
	"TibetanClassicSkt4": {"maxc": 255},
	"DzongkhaCalligraphic": {"maxc": 255},
	"DzongkhaCalligraphicSkt1": {"maxc": 255},
	"DzongkhaCalligraphicSkt2": {"maxc": 255},
	"DzongkhaCalligraphicSkt3": {"maxc": 255},
	"DzongkhaCalligraphicSkt4": {"maxc": 255},
	"Sama": {"maxc": 255},
	"Esama": {"maxc": 255},
	"Samb": {"maxc": 255},
	"Esamb": {"maxc": 255},
	"Samc": {"maxc": 255},
	"Esamc": {"maxc": 255},
	"Ltibetan": {"maxc": 255},
	"LTibetanExtension": {"maxc": 255},
	"LMantra": {"maxc": 255}
}

font_list_udp = {
	"Ededris-syma": {"maxc": 127},
	"Ededris-vowa": {"maxc": 127},
	"Ededris-a": {"maxc": 127},
	"Ededris-a1": {"maxc": 127},
	"Ededris-a2": {"maxc": 127},
	"Ededris-a3": {"maxc": 127},
	"Ededris-b": {"maxc": 127},
	"Ededris-b1": {"maxc": 127},
	"Ededris-b2": {"maxc": 127},
	"Ededris-b3": {"maxc": 127},
	"Ededris-c": {"maxc": 127},
	"Ededris-c1": {"maxc": 127},
	"Ededris-c2": {"maxc": 127},
	"Ededris-c3": {"maxc": 127},
	"Ededris-d": {"maxc": 127},
	"Ededris-d1": {"maxc": 127},
	"Ededris-d2": {"maxc": 127},
	"Ededris-d3": {"maxc": 127},
	"Ededris-e": {"maxc": 127},
	"Ededris-e1": {"maxc": 127},
	"Ededris-e2": {"maxc": 127},
	"Ededris-e3": {"maxc": 127},
	"Ededris-f": {"maxc": 127},
	"Ededris-f1": {"maxc": 127},
	"Ededris-f2": {"maxc": 127},
	"Ededris-f3": {"maxc": 127},
	"Ededris-g": {"maxc": 127},
	"Ededris-g1": {"maxc": 127},
	"Ededris-g2": {"maxc": 127},
	"Ededris-g3": {"maxc": 127},
	"Dedris-syma": {"maxc": 127},
	"Dedris-vowa": {"maxc": 127},
	"Dedris-a": {"maxc": 127},
	"Dedris-a1": {"maxc": 127},
	"Dedris-a2": {"maxc": 127},
	"Dedris-a3": {"maxc": 127},
	"Dedris-b": {"maxc": 127},
	"Dedris-b1": {"maxc": 127},
	"Dedris-b2": {"maxc": 127},
	"Dedris-b3": {"maxc": 127},
	"Dedris-c": {"maxc": 127},
	"Dedris-c1": {"maxc": 127},
	"Dedris-c2": {"maxc": 127},
	"Dedris-c3": {"maxc": 127},
	"Dedris-d": {"maxc": 127},
	"Dedris-d1": {"maxc": 127},
	"Dedris-d2": {"maxc": 127},
	"Dedris-d3": {"maxc": 127},
	"Dedris-e": {"maxc": 127},
	"Dedris-e1": {"maxc": 127},
	"Dedris-e2": {"maxc": 127},
	"Dedris-e3": {"maxc": 127},
	"Dedris-f": {"maxc": 127},
	"Dedris-f1": {"maxc": 127},
	"Dedris-f2": {"maxc": 127},
	"Dedris-f3": {"maxc": 127},
	"Dedris-g": {"maxc": 127},
	"Dedris-g1": {"maxc": 127},
	"Dedris-g2": {"maxc": 127},
	"Dedris-g3": {"maxc": 127},
	"TCRC Bod-Yig": {"maxc": 255},
	"TCRC Youtso": {"maxc": 255},
	"TCRC Youtsoweb": {"maxc": 255},
	"Monlam ouchan 1": {"maxc": 255},
	"Monlam ouchan 2": {"maxc": 255},
	"Monlam ouchan 3": {"maxc": 255},
	"Monlam ouchan 4": {"maxc": 255},
	"Monlam yigchong": {"maxc": 255},
	"TibetanCalligraphic": {"maxc": 255},
	"TibetanCalligraphicSkt1": {"maxc": 255},
	"TibetanCalligraphicSkt2": {"maxc": 255},
	"TibetanCalligraphicSkt3": {"maxc": 255},
	"TibetanCalligraphicSkt4": {"maxc": 255},
	"TibetanClassic": {"maxc": 255},
	"TibetanClassicSkt1": {"maxc": 255},
	"TibetanClassicSkt2": {"maxc": 255},
	"TibetanClassicSkt3": {"maxc": 255},
	"TibetanClassicSkt4": {"maxc": 255},
	"DzongkhaCalligraphic": {"maxc": 255},
	"DzongkhaCalligraphicSkt1": {"maxc": 255},
	"DzongkhaCalligraphicSkt2": {"maxc": 255},
	"DzongkhaCalligraphicSkt3": {"maxc": 255},
	"DzongkhaCalligraphicSkt4": {"maxc": 255},
	"Sama": {"maxc": 255},
	"Esama": {"maxc": 255},
	"Samb": {"maxc": 255},
	"Esamb": {"maxc": 255},
	"Samc": {"maxc": 255},
	"Esamc": {"maxc": 255},
	"Ltibetan": {"maxc": 255},
	"LTibetanExtension": {"maxc": 255},
	"LMantra": {"maxc": 255},
	"TibetanMachineWeb": {"maxc": 127},
	"TibetanMachineWeb1": {"maxc": 127},
	"TibetanMachineWeb2": {"maxc": 127},
	"TibetanMachineWeb3": {"maxc": 127},
	"TibetanMachineWeb4": {"maxc": 127},
	"TibetanMachineWeb5": {"maxc": 127},
	"TibetanMachineWeb6": {"maxc": 127},
	"TibetanMachineWeb7": {"maxc": 127},
	"TibetanMachineWeb8": {"maxc": 127},
	"TibetanMachineWeb9": {"maxc": 127},
	# not present:
	#"TibetanMachineSkt1": {"maxc": 255},
	#"TibetanMachineSkt2": {"maxc": 255},
	#"TibetanMachineSkt3": {"maxc": 255},
	#"TibetanMachineSkt4": {"maxc": 255},
	#"TibetanMachine": {"maxc": 255},
	# Tibetan Modern ?
	# Tibetan Machine D ?
}

create_rtf(font_list_attu, "allchars-attu.rtf")
create_rtf(font_list_udp, "allchars-udp.rtf")

