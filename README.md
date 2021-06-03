# CCFv3 Model GEN

This is a repo for scripts that generate 3D models (GLTF, including the draco compressed) based on the CCFv3 annotation(25 times downsampled). CCFv3 is a **C**ommon **C**oordinate **F**ramework for mouse brain data alignment, issued by Allen Institute for Brain Science in 2020 ([The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas](https://pubmed.ncbi.nlm.nih.gov/32386544/)). It is a perfect 3D annotation to make 3D models for mouse brain. Yes, you can build a mouse brain based on an arbitrary mouse brain imaging data like others do, but this framework gives you a very complete and validated annotation of any fine substructures of the mouse brain, and the most distinct feature is, the model is useful for data from any mouse brain, long as these data are aligned to this framework, which allows you to meaningfully compare data from different sources in the same picture. Sometimes, you have only data representing some brain regions rather than exact spatial locations, then forget about the alignment, you only need to know the id or name of the brain region you are interested in.

Our scripts use mayavi to get wavefront models from the annotation, using the table of annotation id and the annotation image. The wavefront version is so large and clumsy that we have to convert it to GLTF (reducing by half). To further make it efficient on web, we compress the GLTF using draco algorithm provided by Google, which gives a very nice result (reduced to only 2% of the wavefront on average, perfect for web usage). You can find the draco version looks still GLTF--its structure maintains, but its buffer changes, so you can't open it directly. Yet, there are, in this workflow, still some issues, like the GLTF conversion tools can't handle too big wavefront files, and some annotations entail so many brain ids that the scripts can get stuck. These are to be solved.

After all, you may find the models generated are a bit 'ugly', which is caused by the downsampling. The original annotation is nice but a bit too large to handle. A proper solution may be to refine the model after the reconstruction, or build a more capable pipeline running on powerful workstations.

Good luck.

by Zuohan Zhao, Southeast University Allen Joint Center, Nanjing, 2020/6

