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

plt.title("Enzo-P Cosmology Weak Scaling on Blue Waters")
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
#m[4096]='o'
#m[4096]='D'

# 16 24 32 48 64
c = {} # colors
#c[24] = 'r'
c[32] = 'g'
#c[48] = 'b'
#c[64] = 'm'

# colors by problem size per core
cn = {}
cn[32768] = 'r'
cn[65536] = 'g'
cn[131072] = 'b'
cn[262144] = 'm'
cn[524288] = 'c'
cn[1048576] = 'y'
cn[2097152] = 'tab:brown'
cn[4194304] = 'tab:orange'



t = data_scale[:,3] # Time

m_b32 = b == 32;
m_n256 = n == 256;

# markers

# strong
# for i_n in [256,384,512,768,1024,1536,2048,3072,4096]:
#     for i_b in [24,32,48,64]:
#        index=( (b==i_b) & (n==i_n));
#        if (len(p[index]) > 1):
#           plt.plot(p[index],0.5*t[index], color=c[i_b], marker=m[i_n], linewidth=2.0)

# weak
P={}
P[15]=16
P[30]=32
P[75]=64
P[135]=128
P[270]=258
P[525]=512
P[1035]=1024
P[2055]=2048
P[4110]=4096
P[8205]=8192
P[16384]=16384
P[16395]=16384
P[32768]=32768
P[32775]=32768
P[65550]=65536
P[131085]=131072
for i in xrange(0,len(p)):
    for j in xrange(i+1,len(p)):
        if (P[p[i]]*8 == P[p[j]] and n[i]*2 == n[j] and b[i] == b[j]):
            c_i=n[j]*n[j]*n[j]/P[p[j]];
            plt.plot(array([p[i],p[j]]),array([t[i],t[j]]),color=cn[c_i],linestyle='solid')
            plt.plot(p[i],t[i],color=cn[c_i],marker=m[n[i]]);
            plt.plot(p[j],t[j],color=cn[c_i],marker=m[n[j]]);

# create legend
i=0
#for i_b in [32]:
#   plt.plot(0,0, label='B'+str(i_b),color=c[i_b], marker=' ')
for i_n in [64,128,256,512,1024,2048]:
    plt.plot(0,0, label='N'+str(i_n),marker=m[i_n],color='k',linestyle='')

# i=0
# for i in range(0,len(p)):
#     plt.plot(p[i],t[i], linestyle='None', color=c[b[i]],marker=m[n[i]])

lg=plt.legend(loc='lower right', ncol=3,prop={'size':10})
lg.get_frame().set_linewidth(2.0)
print ("Writing 'smp-cosmo-weak'")
plt.savefig("smp-cosmo-weak.png", format='png')
plt.savefig("smp-cosmo-weak.pdf", format='pdf')

# ----------------------------------------------------------------------
