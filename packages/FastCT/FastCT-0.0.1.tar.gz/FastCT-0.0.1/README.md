# FastCT: CT scan and Radon transform
```
scan(A):
  fast Radon transform
  A = image data (shape(n,n,...))
  return scanned image (shape(2n,n,4,...))
  n must be power of 2

BackScan(A):
  inverse fast Radon transform
  A = scanned and filtered data (shape(2n,n,4,...))
  return image restored from A (shape(n,n,...))
  n must be power of 2

filtering(A):
  apply high-pass filter along first axis
  A = scanned image (shape(:,:,...))
  return filtered image (same shape as A)

reconstruct(A):
  return BackScan(filtering(A))

stitch(A):
  stitch four quadrants of scanned data
  A = scanned image (shape(2n,n,4,...))
  return scanned image (shape(2n,4n,...))

RadonFromSinogram(A, n=None):
  A = scanned image (shape(N,M,...))
      first and second axis of A corresponds to r and
      theta coordinate of Radon Transform, respectively
      assume r uniformly increases in [0, sqrt(M*M+N*N)/2)
         theta uniformly increases in [0, pi)
  n = image size
  if n is None, n is set to N/2
  return scanned image (shape(2n,n,4,...))
         to be input to BackScan()

SinogramFromRadon(A, N=None, M=None):
  inverse of RadonFromSinogram
  if N is None, N is set to A.shape[1]*2
  if M is None, M is set to A.shape[1]*4

-------------------------------------------------------------
referece:
  M. L. Brady, "A Fast Discrete Approximation Algorithm for the
    Radon Transform" SIAM Journal on Computing 27 (1998) 107
  W. H. Press, "Dicrete Radon Transform has an Exact, Fast Inverse..."
    Proceedings of the National Academy of Sciences 103 (2006) 19249
```
# example code:
```
import numpy as np
import matplotlib.pyplot as plt
from FastCT import scan,stitch,reconstruct

A = plt.imread('image.png')[:,:,0]
A = scan(A)
plt.imsave('scan.png', stitch(A), cmap='gray')
A = reconstruct(A)
plt.imsave('recon.png', A, cmap='gray')
```