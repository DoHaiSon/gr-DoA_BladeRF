# gr-DoA_BladeRF
Blocks for GNU Radio to DoA by BladeRF

Project made by Do Hai Son in 2020. (Tested on BladeRF x115).

# Installation

The description of the installation is focussed on Ubuntu distribution and its flavours. First make sure that you have all required packages (checked on Ubuntu 16.04 and 18.04):

- GNU Radio 3.7 ( I'll convert to 3.8 if someone needs it).
- BladeRF lib, client: [https://github.com/Nuand/bladeRF](https://github.com/Nuand/bladeRF).
- FPGA lastest loaded BladeRF.

To compile and install gr-DoA_BladeRF run:

cd gr-DoA_BladeRF

mkdir build

cmake ..

make

sudo make install

# Usage

Run DoA.grc in /apps

Change parameters for your system.

Thanks so much for ideas and some Blocks made by [S. Whiting, D. Sorensen, T. K. Moon và J. H. Gunther](https://github.com/samwhiting/gnuradio-doa)

Thanks my monitor in this Project: Dr. Tran Thi Thuy Quynh at Laboratory of Faculty of Electronics and Telecommunications, University of Engineering and Technology, Vietnam National University, Hanoi.

# *We encourage you to also perform reproducible research!. If you use these code, please acknowledge the following papers*:

- Do Hai, Son and Tran Thi Thuy, Quynh, "Đồng bộ nhiều SDR trong thực thi thuật toán ước lượng hướng sóng đến MUSIC," in *Hội nghị Quốc gia lần thứ XXIV về Điện tử, Truyền thông và Công nghệ Thông tin*, Ha Noi, VietNam, 2021.

License and Referencing These code is licensed under the GPLv2 license. If you in any way use these code for research that results in publications, please cite our original article listed above.
