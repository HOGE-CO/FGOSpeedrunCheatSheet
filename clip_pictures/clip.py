import cv2
import os
import sys

# constants
DEFAULT_DIR_NAME = 'result_img'
CLIP_BEGIN_X = 0
CLIP_END_X = 1596
CLIP_BEGIN_Y = 258
CLIP_END_Y = 1416

def check_args():
    usage = 'Usage: python3 {} SOURCE_IMAGE_DIR [optional: OUTPUT_DIR]'.format(__file__)
    if len(sys.argv) == 1:
        return usage
    else:
        return ''

def create_output_dir(src):
    if src == '' or src[0] != '/':
        print('needs absolute path for output results')
        sys.exit()
    
    os.makedirs(src, exist_ok=True)

def conv_dir_abs(src):
    suffix = '' if src[-1] == '/' else '/' 
    if src[0] != '/':
        return os.getcwd() + '/' + src + suffix
    else:
        return src + suffix

def clip_img(src_path, out_path, src_file_name):
    img = cv2.imread(src_path + src_file_name)
    if img is None:
        print('cannot open file {}'.format(src_path + src_file_name))
        sys.exit()

    clipped_img = img[CLIP_BEGIN_Y : CLIP_END_Y, CLIP_BEGIN_X : CLIP_END_X]
    cv2.imwrite(out_path + src_file_name, clipped_img)

    return

if __name__ == '__main__':
    # check argments
    check_arg_result = check_args()
    if check_arg_result != '':
        print(check_arg_result)
        sys.exit()
    
    # create output dir
    src_path = conv_dir_abs(sys.argv[1])
    out_path = conv_dir_abs(DEFAULT_DIR_NAME) if len(sys.argv) == 2 else conv_dir_abs(sys.argv[2])
    create_output_dir(out_path)

    # get file list
    file_list = [file.name for file in os.scandir(src_path) if file.is_file()]
    for file_name in file_list:
        clip_img(src_path, out_path, file_name)

    sys.exit()
