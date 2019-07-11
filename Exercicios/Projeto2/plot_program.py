import matplotlib.pylab as plt                                           # It allows doing plots using the matplotlib package
plt.rcParams['figure.figsize'] = (30.0, 30.0)                            # It determines the plot size inside ipython notebook
from astropy.io import fits, votable                                     # It allows loading files 'fits' and 'votable'
from astropy.table import Table                                          # It allows loading tables 
from astropy import wcs                                                  # It imports the World Coordinate System (WCS) package
import numpy as np                                                       # It imports the numpy package
from lambda_rest_function import lambda_rest                             # Importing the module with the function lambda_rest

# Defining a function that works individually for each file and saving the content of each file in an astropy.io.fits object:
hdulist = fits.open('stPC1+2_GS2.fits')

# Importing the tables of the slits and the emission lines:
table1 = np.loadtxt('slits_table.txt',dtype={'names':('slit','redshift','separation','height','line1','line2','line3','line4'),'formats':('i4','f8','i4','f8','i4','i4','i4','i4')},unpack=True,delimiter=',')
    
slit = table1[0]
redshift = table1[1]
separation = table1[2]
height = table1[3]
line1 = table1[4]
line2 = table1[5]
line3 = table1[6]
line4 = table1[7]

table2 = np.loadtxt('emission_lines_table.txt',dtype={'names':('name','rest_lambda'),'formats':('S12','i4')},unpack=True,delimiter=',')

name = table2[0]
rest_lambda = table2[1]
    
# Loading the images:
for i in range(0,len(slit)):
    img = hdulist[i+1].data
    
# Saving the header of the file slits in 'header':
    header = hdulist[i+1].header  
    print('THE 2D SPECTRUM OF SLIT' + str(i+1) + ':')

# Establishing the x-axis: 
    npix = header['NAXIS1']
    pixsize = header['CDELT1']
    startwave = header['CRVAL1']
    print('npix =', npix, ', pixsize =', pixsize, ', startwave =', startwave)

    wave = (np.arange(npix) * pixsize + startwave)
    xleft = wave[0]
    xright = wave[-1]
    print('Wavelength axis from ', xleft, ' to ' , xright)

# Establishing the y-axis: 
    npix2 = header['NAXIS2']
    pixsize2 = header['CDELT2']
    startpixel = header['CRVAL2']
    print('npix2 =', npix2, ', pixsize2 =', pixsize2, ', startpixel =', startpixel)

    pixel = (np.arange(npix2) * pixsize2 + startpixel)
    ylower = pixel[0]
    yupper = pixel[-1]
    print('Pixel axis from ', ylower, ' to ', yupper, '\n')

# Defining low and high:
    neg_img = -1*img
    box = [500,1500,5,20]
    sel_box = neg_img[box[2]:box[3],box[0]:box[1]]
    median_pixel = np.median(sel_box)
    sd_pixel = np.std(sel_box)
    low = median_pixel - 3 * sd_pixel
    high = median_pixel + 0.5 * sd_pixel

# Putting vertical lines in the regions where emission lines are expected, putting circles in the regions where emission lines were detected, 
# creating the new x-axis at the top and plotting the 2D spectra:
    z = redshift[i]
    detected_lines = [line1[i],line2[i],line3[i],line4[i]]
    fig = plt.figure(figsize=(30,6))
    ax1 = fig.add_subplot(111)
    ax1.imshow(neg_img, vmin=low, vmax=high, cmap='gray', origin='lower', extent=(xleft,xright,ylower,yupper))
    lambda_obs = np.arange(xleft,xright,separation[i])
    ax1.set_xticks(lambda_obs)
        
    for j in range(0,len(name)):
        if z != 0:  
            xcoords = [(1+z)*rest_lambda[j]]
            for xc in xcoords:
                if xc < xright and xc > xleft:
                    plt.axvline(xc, color='r', lw=1.5, linestyle=':')
                        
    for k in range(0,len(detected_lines)):
        if detected_lines[k] != 99:
            circle = plt.Circle((detected_lines[k], 12), 20, color='r', fill=False, lw=1)
            ax = fig.gca()
            ax.add_artist(circle)
                
    ax2 = fig.add_axes(ax1.get_position(),frameon=False)
    ax2.tick_params(labelbottom='off', labeltop='on', labelleft='off', labelright='off', bottom='off', left='off', right='off')
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(lambda_obs)
    ax2.set_xticklabels(lambda_rest(lambda_obs,z), minor=False)
    plt.draw()
    ax2.set_position(ax1.get_position())

    ax1.set_xlabel('$\lambda_{obs}$ ($\AA$)',fontsize=14)
    ax1.set_ylabel('pixels',fontsize=12)
    ax1.set_title('$\lambda_{rest}$ ($\AA$)',fontsize=14)
    plt.title('slit'+str(i+1),y=height[i],fontsize=14)
    plt.show()
