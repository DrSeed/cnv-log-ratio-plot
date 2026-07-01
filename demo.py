import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(7);nb=3000
lr=rng.normal(0,0.15,nb)
lr[600:800]+=0.8   # amplification
lr[1500:1700]-=1.0 # deletion
chrom=np.repeat(np.arange(1,11),300)
plt.figure(figsize=(11,3.5))
for c in range(1,11):
    m=chrom==c;plt.scatter(np.where(m)[0],lr[m],s=3,c=["#4c72b0","#c44e52"][c%2])
plt.axhline(0,c="k",lw=.7);plt.xlabel("genomic bin");plt.ylabel("log2 copy-number ratio")
plt.title("Copy-number profile (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("1 amplification + 1 deletion\n");print("ok")