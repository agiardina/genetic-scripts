from pandas_plink import read_plink1_bin
import math

G = read_plink1_bin("SLI1c1.bed", "SLI1c1.bim", "SLI1c1.fam", verbose=False)
samples = G.sample
for sample in samples:
    s = sample.values
    values = list(G.sel(sample=s).values)
    tot = len(values)
    missing_values = list(filter(lambda x: math.isnan(x),values))
    missing = len(missing_values)
    print(s, missing/tot)
