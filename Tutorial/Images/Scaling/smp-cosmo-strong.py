#!/usr/bin/python

from numpy import *
import numpy as np
import matplotlib.pyplot as plt

color = ['c','m','k','r','g','b','y']
marker = ['x','o']

#plt.figure(figsize=(10.5,7.5));
plt.figure(figsize=(7,5));
plt.xlabel("Processing units (FP cores)")
plt.xscale('log', basex=2)
plt.yscale('log', basey=2)
plt.grid(True)
plt.xlim(2**(3),2**18);
plt.ylim(2**(-4),2**8);

# ----------------------------------------------------------------------

plt.title("Enzo-P Cosmology Strong Scaling on Blue Waters")
plt.ylabel("Time per cycle (s)")

data_scale = loadtxt('smp-cosmo.data',dtype=float)

p = data_scale[:,0] # Processors (cores)
n = data_scale[:,1] # Problem size n^3
# 64 96 128 192 256 384 512 768 1024 1536 2048
b = data_scale[:,2] # Block size b^3
m = {} # markers
m[32]='>'
m[64]='+'
m[128]='^'
m[256]='x'
m[512]='<'
m[1024]='*'
m[2048]='v'
#m[3072]='o'
#m[4096]='D'

# 16 24 32 48 64
c = {} # colors
#c[24] = 'r'
c[32] = 'g'
#c[48] = 'b'
#c[64] = 'm'

# colors by problem size
cn = {}
cn[32] = 'r'
cn[64] = 'g'
cn[128] = 'b'
cn[256] = 'm'
cn[512] = 'c'
cn[1024] = 'y'
cn[2048] = 'k'

t = data_scale[:,3] # Time

# markers

# strong
for i_n in [32,64,128,256,512,1024,2048]:
    for i_b in [32]:
       index=( (b==i_b) & (n==i_n));
       if (len(p[index]) > 1):
          plt.plot(p[index],t[index], color=cn[i_n], marker=m[i_n], linewidth=2.0)

# weak
#for i in xrange(0,len(p)):
#    for j in xrange(i+1,len(p)):
#        if (pr[p[i]]*8 == pr[p[j]] and n[i]*2 == n[j] and b[i] == b[j]):
#            plt.plot(array([p[i],p[j]]),array([t[i],t[j]]),color=c[b[i]],linestyle='dashed')
#            plt.plot(p[i],t[i],color=c[b[i]],marker=m[n[i]]);
#            plt.plot(p[j],t[j],color=c[b[j]],marker=m[n[j]]);

# create legend
#for i_b in [32]:
#    plt.plot(0,0, label='B'+str(i_b),color='k', marker=' ')
for i_n in [64,128,256,512,1024,2048]:
    plt.plot(0,0, label='N'+str(i_n),marker=m[i_n],color='k',linestyle='')


lg=plt.legend(loc='lower right', ncol=3,prop={'size':10})
lg.get_frame().set_linewidth(2.0)
print ("Writing 'smp-cosmo-strong'")
plt.savefig("smp-cosmo-strong.png", format='png')
plt.savefig("smp-cosmo-strong.pdf", format='pdf')

# ----------------------------------------------------------------------
