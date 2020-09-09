#tensors, index starts from zero ;)
import torch

#1D
x=torch.ones(3) #1d tensor of size 3;three 1's
y=torch.zeros(3) #same's for zeros 
y[1]=5 #tensor([0., 5., 0.])
my_tensor=torch.tensor([1,2,3,]) #tensor([1, 2, 3])

#2D
two_di=torch.tensor([[1,2],[3,4]])
'''tensor([[1, 2],
        [3, 4]])'''
print(two_di[1,0]) #prints tensor(3) 
print(two_di[1]) #tensor([3, 4])
print(two_di.shape)#torch.Size([2, 2]) format [row,col]
two_di[None]
'''tensor([[[1, 2],
         [3, 4]]])'''
zeros=torch.zeros(2,3)
'''tensor([[0., 0., 0.],
        [0., 0., 0.]])'''

										#indexing in tensors

#1D
tensor_plusplus=torch.tensor(range(4)) #print tensor([0, 1, 2, 3])
tensor_plusplus[:] #tensor([0, 1, 2])
tensor_plusplus[-1] #tensor(3)
tensor_plusplus[:-1] #tensor([0, 1, 2]); excludes the last element
tensor_plusplus[::2] #tensor([0, 2]); printing elements with step 2. Default val of step is 1.

#2D
good_boy=torch.tensor([[1,2,3,],[4,5,6]])
'''tensor([[1, 2, 3],
        [4, 5, 6]])'''
good_boy[None] #the same as above 
good_boy[:,1] #tensor([2, 5]); prints first col of the tensor; Format [row from:til row-1,col from: til col-1]
good_boy[1,1:] #tensor([5, 6])
good_boy.reshape(1,6) #tensor([[1, 2, 3, 4, 5, 6]])


										#operations
x=torch.tensor(torch.ones(4)) #tensor([1., 1., 1., 1.])
x=torch.ones(4).int() #tensor([1, 1, 1, 1], dtype=torch.int32)
torch.sum(x) #tensor(4)
y=torch.tensor([1,2,3,4])
z=torch.tensor([[1,2],[3,4],[5,6]])
'''tensor([[1, 2],
        [3, 4], 
        [5, 6]])'''
z.transpose(0,1)
'''tensor([[1, 3, 5],
        [2, 4, 6]])'''
torch.add(x,y) #tensor([2, 3, 4, 5])
print(x+y) #tensor([2, 3, 4, 5])
torch.sub(x,y) #tensor([ 0, -1, -2, -3]); Other way of doing this is : x-y
torch.mul(x,y) #tensor([1, 2, 3, 4]); Same as x*y and x.mul(y);element by element mat mul.
abc=torch.tensor([[1,2,3],[3,4,5]])



								#transposing in higher dimensions

abc=torch.tensor([[1,2,3],[3,4,5]])
abc_t=abc.t() #transposing a tensor; only for dimensions >=2
'''tensor([[1, 3],
        [2, 4],
        [3, 5]])'''
#transposing matrix in multidimensions
demo=torch.ones(3,4,5)
demo.shape #torch.Size([3, 4, 5])
demo_t=demo.transpose(1,2)
demo_t.shape #torch.Size([3, 5, 4])

								#numpy - tensor interoperability 

tensor=torch.tensor(torch.ones(5)) #tensor([1., 1., 1., 1., 1.])
tensor_to_np=tensor.numpy() #array([1., 1., 1., 1., 1.], dtype=float32)
t=torch.from_numpy(tensor_to_np) #tensor([1., 1., 1., 1., 1.])

								#saving tensors
import h5py
f=h5py.File('storing_tensor.hdf5','w')
f.create_dataset('dataset',data=t)
f.close()
read=h5py.File('storing_tensor.hdf5','r')
read.keys() #<KeysViewHDF5 ['dataset']>
read.values() #ValuesViewHDF5(<HDF5 file "storing_tensor.hdf5" (mode r)>)
print(read.get('dataset')) #<HDF5 dataset "dataset": shape (5,), type "<f4">
read.close()










#exercise

