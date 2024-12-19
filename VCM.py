import math
names = locals()

hh      =   0.2e-3
ld      =   1e-3
ww      =   0.5e-3
seta    =   120
phi     =   60
sigma   =   0.066

kk      =   72.72
nn      =   0.181-1
mm      =   0.0734

seta    =   (seta/180)*math.pi
phi     =   (phi/180)*math.pi

lsif    =   ww * -0.5 + ld * -0

test    =   0

delta   =   1e-9

print('u_s  Q  hr  eta')

for i in range(60):
    uu = (i+1) * 0.01

    gama    =   uu/hh
    eta     =   kk*(gama**nn)+mm

    h0 = hh * 0.1
    hm = hh * 1.6

    while True:
        test    +=  1
        hw      =   (h0+hm)/2
        ca      =   eta*uu/sigma
        ls1x    =   (hh**2)/(6*eta*uu)
        ls1y1   =   -1.34*(ca**(2/3))*sigma/hw
        ls1y2   =   (sigma/hh)*(math.cos(seta)+math.cos(phi))
        ls2     =   ld*(1-(2*hw/hh))
        ls      =   ls1x*(ls1y1+ls1y2)+ls2

        if ls-lsif > delta:
            h0      =   hw

        elif ls-lsif < -delta:
            hm      =   hw

        else:
            line    =   str('%.3g' % uu) +' '+ str('%.3g' % (hw*uu*50e-3*1e6)) +' '\
                        +str('%.6g' % (hw/hh)) +' '+str('%.3g' % eta)
            print(line)
            break
