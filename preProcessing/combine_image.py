import glob
import cv2 as cv


paths = glob.glob('./data/res(02828884)/*')
count = 0
for pt in paths:
    for i in range(0, 84):
        illumination = cv.imread(glob.glob(pt + '/I_output_' + str(i) + '.png')[0])
        albedo = cv.imread(glob.glob(pt + '/A_output_' + str(i%12) + '.png')[0])
        normal = cv.imread(glob.glob(pt + '/N_output_' + str(i%12) + '.png')[0])

        cv.imwrite('./afterPre/data1/' + str(count) + '.png', cv.hconcat([normal, illumination]))
        cv.imwrite('./afterPre/data2/' + str(count) + '.png', cv.hconcat([normal, albedo]))
        count += 1
        print(count)

