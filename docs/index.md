
# Welcome to Richie Honor's portfolio! 

#### Here you can view the figures I have created, my data analyses and other examples of code that contributed to various projects. The links to my published works are also included as links when available. 

## **[Gallery](richiehonor.github.io/Gallery.html)**



## **R Projects**



* **[Figure generation for "EICA 2.0: A general theory of enemy release in plant invasions"](richiehonor.github.io/EICA2_SuppMat.html) *(published book chapter)*** 

*Here is the code used to generate the figures for my recently published (2020) chapter in the book ["Plant invasions: the role of biotic interactions"](https://www.cabi.org/cabebooks/ebook/20203555905). There also contains a few figures that were not used in the final manuscript, but were part of the process.*




 * **[Data analysis and visualization for "Assessing the prevalence and correlates of antenatal cannabis consumption in an urban Canadian population: A cross-sectional survey"](richiehonor.github.io/Kaarid_et_al_2021_SupplementaryMaterial.html) *(acientific article)***

*Here is the code used to perform the statistical analysis and generate the figures involved for this medical study. This was a collaboration between myself and medical researchers at McMaster University in Hamilton ontario. This article is currently in review with the journal [CMAJ Open](http://cmajopen.ca).*




 * **[Data integration for "Plasticity and evolutionary potential of *Alliaria petiolata* life history and leaf chemistry traits in different competitive environments"](richiehonor.github.io/AllData_Synthesis.html) *(MSc thesis)***

*Here is the code used to integrate 11 different data files into one file from which data analysis and visualization were performed (see below). This data was used in the publishing of my [master's thesis](https://qspace.library.queensu.ca/handle/1974/28610).*





## **Python Projects**


* **[Organising unstructured UV spectroscopy data](UV-Docs/UVSpec_Portfolio.html)**

UV spectroscopy machines in laboratories are frequenly old - they can be found runing on windows XP with a sticky note attached to the monitor reading: "DO NOT UPDATE". The typical output of the machine is spectroscopy data from various wavelength corresponding to 96 unique samples, yield hundreds of data points that must be organised [(for example)](UV-Docs/Dat_Dec_6_2019.txt). While this is typically done manually, I needed to peform >50 runs, which would have costed me a large amount of time. I designed two programs in python in order to build a [single data frame](UV-Docs/All_UV_Data.txt) out of the unstructured output files of the machine for later analysis in R.





* **[Extracting growth rate data from photos using machine learning](Machine_Learning_Portfolio.html)**

How does one measure the size of each leaf on >600 plants every two weeks for 2 months? Either by spending two months in the greenhouse or by developping software to do it for you. I designed software to take photos two photos of a plant (top and side view) and assign the photos with the name corresponding to the genotype of the plant using a barcoder. I then used machine learning to train the computer to identify plant from background using the packages opencv2 and plantcv, and I extracted data pertaining to plant size. This program was run over multiple directories with >5000 images to store the data from all the photos into a single data file to be used in later analyses of growth rate. 















