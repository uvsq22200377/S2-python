import pandas
info_villes=pandas.read_csv("ville_virgule.csv")
densité=info_villes.loc[(info_villes["dens"]<=500)]