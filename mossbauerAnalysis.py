import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import logging
import os

class Analyzer:
    def __init__(self, data, size, compound, calibrationVelocity):
        self.name = compound
        compoundNameList = compound.split("_")
        self.compoundName = " ".join(compoundNameList)
        self.data = pd.read_fwf(data)
        self.counts = self.data["Counts"]
        self.size = size
        self.half = int(self.size/2)
        self.left = np.flip(np.array(self.data[0:self.half-1]))
        self.right = np.array(self.data[self.half:])
        self.CalibratedVelocity = calibrationVelocity

    def check_and_create_folder(self):
        print(f"Analysis started for {self.compoundName}")
        if not os.path.exists(self.name):
            os.makedirs(self.name)
            logging.info(f"Folder Created for {self.compoundName}")
            print(f"-->Folder '{self.name}' created.")
        else:
            logging.info(f"Folder Already Exists for {self.compoundName}")
            print(f"-->Folder '{self.name}' already exists.")

    def spectrumFolder(self):
        self.folded = np.ravel(self.left + self.right)
        foldedData = pd.DataFrame({"Velocity": np.linspace(-9.48105, 9.32983, len(self.folded)), "Counts": self.folded})
        foldedData.to_csv(f"{self.name}/{self.name}_Folded.txt", sep=",", mode="w", header=True, index=False)

    def spectrumPlotter(self):

        self.spectrumFolder()

        fig, ax = plt.subplots()
        x = np.linspace(0, self.size, self.size - 1)
        ax.scatter(x, self.counts, s=1)
        ax.set_ylim(min(self.counts)-100, np.sort(self.counts)[-2]+300)
        fig.savefig(f"{self.name}/rawPlot.pdf", dpi=300, bbox_inches="tight")
        print("-->Raw Spectrum Plotted")

        fig, ax = plt.subplots()
        x1 = np.linspace(0, self.half, self.half-1)
        ax.scatter(x1, self.folded, s=1)
        ax.set_ylim(min(self.folded)-100, np.sort(self.folded)[-2]+300)
        centroid = np.mean(x1)
        ax.vlines(centroid, min(self.folded)-100, np.sort(self.folded)[-2]+300, ls="-", alpha=0.5, color="red")
        ax.vlines(x1[np.where(self.folded == min(self.folded))[0]],  min(self.folded)-100, np.sort(self.folded)[-2]+300,
                  ls="-", alpha=0.5, color="green")
        ax.set_title("Folded Spectrum")
        ax.set_xlabel("Channel")
        ax.set_ylabel("Counts")
        fig.savefig(f"{self.name}/foldedPlot.pdf", dpi=300, bbox_inches="tight")
        print("-->Folded Spectrum Plotted")

        x2 = x1 * self.CalibratedVelocity - 9.5
        x4 = np.linspace(-9.48105, 9.32983, len(self.folded))
        fig, ax = plt.subplots()
        ax.set_xlabel("Velocity [mm s$^{-1}$]")
        ax.set_ylabel("Counts")
        ax.set_title(f"Mössbauer Spectrum for {self.compoundName}")
        ax.scatter(x4, self.folded, s=1)
        ax.set_ylim(np.sort(self.folded)[1]-100, np.sort(self.folded)[-2]+300)
        fig.savefig(f"{self.name}/calibratedPlot.pdf", dpi=300, bbox_inches="tight")
        print("-->Calibrated Folded Spectrum Plotted")

        print(f"Analysis done for {self.compoundName}")
