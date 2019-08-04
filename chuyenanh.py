##thanks to DEVED for the support
import imageio
import os

clip = os.path.abspath('clip.mp4')


def pictogif(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    print(f'Dang chuyen {inputPath} \n toi {outputPath}')
    docanh = imageio.get_reader(inputPath)
    fps = docanh.get_meta_data()['fps']
    writer = imageio.get_writer(outputPath, fps=fps)
    for frames in docanh:
        writer.append_data(frames)
        print(f'Dang chay Frame {frames} ')
    print('Hoan thanh')
    writer.close()


pictogif(clip, '.gif')
