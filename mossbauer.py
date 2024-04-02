from mossbauerAnalysis import Analyzer

datFile = "Iron57.TKA"
datFile1 = "Hydrated_Iron_Sulfate.TKA"

ps5 = Analyzer(datFile, 1024, "Iron_57", 0.0367482758621)
ps6 = Analyzer(datFile1, 1024, "Hydrated_Iron_Sulfate", 0.0367482758621)

def main():
    ps5.check_and_create_folder()
    ps5.spectrumFolder()
    ps5.spectrumPlotter()

if __name__ == "__main__":
    main()

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
#
# dat = pd.read_fwf("hydratedIronSulfate/Hydrated_Iron_Sulfate.TKA")
# # print(dat)
# left = np.array(dat[0:511])
# right = np.array(dat[512:])
#
# leftFlipped = np.flip(left)
#
# folded = leftFlipped+right
#
# print(len(left))
# print(len(right))
#
# fig, ax = plt.subplots()
# x = np.linspace(0,1024,1023)
# ax.vlines(1023/2, 0,4000)
# # print(len(dat["Counts"]))
# # print(len(x))
# ax.scatter(x, dat["Counts"], s=1)
# ax.set_ylim(6200, 8000)
# fig.savefig("hydratedIronSulfate/plot.jpg", dpi=300, bbox_inches="tight")
#
# fig, ax = plt.subplots()
# x1 = np.linspace(0,512,511)
# ax.scatter(x1, folded, s=1)
# ax.set_ylim(13750, 15000)
# fig.savefig("hydratedIronSulfate/plot1.jpg", dpi=300, bbox_inches="tight")
#
# # ind = np.where(folded < 6100)[0]
# # print(ind)
#
# vCal = 0.0367482758621
# x2 = x1*vCal-9.5
# fig, ax = plt.subplots()
# x1 = np.linspace(0,512,511)
# # ax.vlines(5.3285, 5800,7500, linestyle="--", color="k")
# # ax.vlines(-5.3285, 5800,7500, linestyle="--", color="k")
# # ax.vlines(0, 5800,7500, linestyle="--", color="k")
# # ax.scatter(x2, folded, s=1)
# # ax.set_ylim(5800,7500)
# x4 = np.linspace(-9.48105, 9.32983, len(folded))
# # ax.set_xlim(-10,-10)
# ax.set_xlabel("Velocity [mm s$^{-1}$]")
# ax.set_ylabel("Counts")
# ax.set_title(r"Mössbauer Spectrum for FeSO$_4\cdot$7H$_2$O")
# ax.scatter(x4, folded, s=1)
# ax.set_ylim(13750, 15000)
# fig.savefig("hydratedIronSulfate/plot2.pdf", dpi=300, bbox_inches="tight")

