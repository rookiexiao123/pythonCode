import cv2
import matplotlib.pyplot as plt

# function to display multiple images

def display_multiple_img(images_paths, rows, cols,title):
    
    figure, ax = plt.subplots(nrows=rows,ncols=cols,figsize=(16,8))
    plt.suptitle(title, fontsize=20)
    for ind,image_path in enumerate(images_paths):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 
        try:
            ax.ravel()[ind].imshow(image)
            ax.ravel()[ind].set_axis_off()
        except:
            continue;
    plt.tight_layout()
    plt.show()
