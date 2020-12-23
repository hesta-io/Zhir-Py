-----------------Tesseract V4.1.1------------------
Dirty Run: 89.59% / 84.00%
Denoise+rShadows+Borders: 88.93% / 83.76%
Denoise+Borders: 87.87% / 82.45%
rShadows+Borders: 89.45% / 83.66%
Denoise+rShadows: 91.38% / 85.34% # We conclude that AddBorders is a Bad Practice
rShadows+Denoise: 91.44% / 85.35% ✔️✔️✔️✔️
Denoise+rShadows+Binarize: 91.04% / 84.84%
rShadows+Denoise+Binarize: 91.10% / 84.94%
Denoise+Binarize: 90.46% / 84.86% # We conclude that removeShaddows is neccessary
Denoise+rShadows+Binarize+Skew: 91.10% / 84.96%
rShadows+Denoise+Binarize+Skew: 90.41% / 85.18%
rShadows: 90.94% / 85.22%
Dnoise: 89.57% / 84.04%
Binarize: 89.84% / 84.14%

Best Preproccessing Pipeline is : rShadows+Denoise
