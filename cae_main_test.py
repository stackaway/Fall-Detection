from ae_exp import *


if __name__ == "__main__":
	
	pre_load = '/Users/churnika/Desktop/Projects/Fall-Detection/Models/SDU-Filled/C3D_AE.h5' #Put path to your saved model here!! It will be in Models/{dset}/model_name.h5
	dset = 'UR-Filled'


	if pre_load == None:
		print('No model path given, please update pre_load variable in cae_main_test.py')

	else:
		hor_flip = True
		img_width, img_height = 64,64

		cae_exp = AEExp(pre_load = pre_load, hor_flip = hor_flip, dset = dset,\
			img_width = img_width, img_height = img_height)

		cae_exp.test(raw = False, animate = True)


