import torchvision.datasets as dset

path2data="./data/train2014"
path2json="./data/annotations/instances_train2014.json"

coco_train = dset.CocoDetection(root = path2data,
                                annFile = path2json)

print('Number of samples: ', len(coco_train))