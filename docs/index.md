<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-54BX40JXLL"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-54BX40JXLL');
</script>


# Welcome to Richie Honor's portfolio! 

#### Here you can view the figures I have created, my data analyses and other examples of code that contributed to various projects. The links to my published works are also included when available. 



## **Gallery**
[Click here for examples of the figures I have created](richiehonor.github.io/Gallery.html)





## **Python Projects**


* **[Organising unstructured UV spectroscopy data](UV-Docs/UVSpec_Portfolio.html)**

UV spectroscopy machines in laboratories are frequenly old - they can be found runing on windows XP with a sticky note attached to the monitor reading: "DO NOT UPDATE". Typically, 96 samples are run through the machine and each sample is read at different wavelengths. This results in hundreds of data points corresponding to a specific wavelength and sample ID. Unfortunately, the output file containing the data is less than optimal [(for example)](UV-Docs/Dat_Dec_6_2019.txt). While these data are often manually organised in an excel document for analysis in R, I needed to peform >50 runs, which would have costed me a large amount of time and left me susceptible to human error. I designed two programs in python in order to build a [single data frame](UV-Docs/All_UV_Data.txt) from all the unstructured UV spectroscopy output files for later analyses in R. This program also circumvents the tedious task of entering each sample ID into the UV-spectroscopy machine by accepting a custom excel file indicating the samples included in the run.





* **[Extracting growth rate data from photos using machine learning](Machine_Learning_Portfolio.html)**

How does one measure the size of each leaf on >600 plants every two weeks for 2 months? Either by spending two months in the greenhouse or by developping software to do it for you. I designed software to take two photos of a plant (one from the top and one from the side) and assign each photo with an ID using a barcoder. I then used machine learning to train the computer to identify plant from background using the packages OpenCV and PlantCV, and I extracted data pertaining to plant size. This program was run over multiple directories with >5000 images. Data from all the photos were extracted and stored in a single data file which was used in later analyses of growth rate in R. 





## **R Projects**



* **[Figure generation for *"EICA 2.0: A general theory of enemy release in plant invasions"*](richiehonor.github.io/EICA2_SuppMat.html)** (published book chapter)

Here is the code used to generate the figures for my recently published (2020) chapter in the book ["Plant invasions: the role of biotic interactions"](https://www.cabi.org/cabebooks/ebook/20203555905). 




 * **[Data analysis and visualization for *"Assessing the prevalence and correlates of antenatal cannabis consumption in an urban Canadian population: A cross-sectional survey"*](richiehonor.github.io/Kaarid_et_al_2021_SupplementaryMaterial.html)** (scientific article)

Here is the code used to perform statistical analyses and generate figures for this medical study. This was a collaboration between myself and medical staff at McMaster University in Hamilton, Ontario. This article is currently in review with the journal [CMAJ Open](http://cmajopen.ca).




 * **[Data integration for *"Plasticity and evolutionary potential of Alliaria petiolata life history and leaf chemistry traits in different competitive environments"*](richiehonor.github.io/AllData_Synthesis.html)** (MSc thesis)

Here is the code used to integrate 11 different data files into one file from which data analysis and visualization were performed. These data were used in the publishing of my [master's thesis](https://qspace.library.queensu.ca/handle/1974/28610).











