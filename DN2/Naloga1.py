#Iz sledečega list-a pridobite vrednost ffff in jo shranite v spremenljivko f_vrednost:
#our_list = ["a", ["bb", "cc"], "d", [["eee"], ["ffff"], "ggg"]]

our_list = ["a", ["bb", "cc"], "d", [["eee"], ["ffff"], "ggg"]]

f_vrednost = our_list[3][1][0]
print("Naša vrednost: " + f_vrednost)
