# id2223-lab2

Download 2014 Coco dataset

```

sudo snap install aria2c
mkdir data; cd data

aria2c -x 10 -j 10 http://images.cocodataset.org/zips/train2014.zip
unzip train2014.zip; rm train2014.zip

aria2c -x 10 -j 10 http://images.cocodataset.org/zips/val2014.zip
unzip val2014.zip; rm val2014.zip

aria2c -x 10 -j 10 http://images.cocodataset.org/annotations/annotations_trainval2014.zip
unzip annotations_trainval2014.zip; annotations_trainval2014.zip


```

Install Coco Python API


```
git clone https://github.com/pdollar/coco.git

cd coco/PythonAPI
sudo make install
sudo python setup.py install

```

