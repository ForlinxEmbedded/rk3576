# FETMX6UL-C简介f是
## 2.1  FETMX6UL-C核心板外观图
	Nand Flash方案：

![](https://cdn.nlark.com/yuque/0/2024/jpeg/45534235/1720509407290-25e8514e-ce6e-4008-b3d5-2fdce3bbfed5.jpeg)

	eMMC方案：

![](https://cdn.nlark.com/yuque/0/2024/jpeg/45534235/1720509407669-be3c40e9-7fec-4f8c-bf93-efd3eded229f.jpeg)

## 2.2  FETMX6UL-C核心板尺寸图
![](https://cdn.nlark.com/yuque/0/2024/png/45534235/1720509408050-e8509073-5452-4af3-b119-813fc5159ebb.png)![](https://cdn.nlark.com/yuque/0/2024/png/45534235/1720509408291-ba416fd5-38ac-4f4b-9979-558373d52271.png)



结构尺寸：40mm×50mm，尺寸公差±0.15mm。

制版工艺：厚度1.15mm，6层沉金PCB。

连接器：双排0.8mm间距，80pin 板对板连接器。具体连接器型号您可直接联系我司销售获取，连接器尺寸图见附录。

核心板与底板固定建议选择M2*5mm的双通铜柱，配套螺钉规格M2*4mm。

## 2.3 性能参数
### 2.3.1  系统主频
| **名称** | **规格** | | | | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
| | **最小** | **典型** | **最大** | **单位** |
| 系统主频 | — | — | 528 | MHz | — |
| 系统RTC时钟 | — | 32.768 | — | KHz | — |


### 2.3.2  供电参数
| **参数** | **引脚标号** | **规格** | | | | **说明** |
| :---: | :---: | :---: | --- | --- | --- | :---: |
| | | **最小** | **典型** | **最大** | **单位** |
| 主电源电压 | VSYS | 4.5 | 5 | 5.5 | V | — |
| 空载电流 | — | 63.1 | — | 85 | mA | — |
| 重载电流 | — | 113 | — | 160 | mA | 视频播放状态 |


### 2.3.3  工作环境
| **参数描述** | | **规格** | | | | **说明** |
| :---: | --- | :---: | --- | --- | --- | :---: |
| | | **最小** | **典型** | **最大** | **单位** |
| 工作温度 | 工作环境 | 0 | 25 | +70 | ℃ | 商业级 |
| | 存储环境 | -40 | 25 | +125 | ℃ | |
| | 工作环境 | -40 | 25 | +85 | ℃ | 工业级 |
| | 存储环境 | -40 | 25 | +125 | ℃ | |
| 湿度 | 工作环境 | 10 | — | 90 | ％RH | 无凝露 |
| | 存储环境 | 5 | — | 95 | ％RH | |


### 2.3.4  核心板接口速度
| **参数** | **规格** | | | | **说明** |
| :---: | :---: | --- | --- | --- | :---: |
| | **最小** | **典型** | **最大** | **单位** |
| 串口通讯速度 | — | 115200 | — | bps | — |
| SPI通讯速度 | — | — | 52 | MHz | — |
| IIC通讯速度 | — | 100 | 400 | Kbps | — |
| CAN通讯速度 | — | — | 1 | Mbps | — |
| SD/MMC/SDIO | — | — | 104 | Mbps | — |
| USB接口速度 | — | — | 480 | Mbps | — |
| AD采集时间 | 0.7 | — | 1.25 | us | Fadc=40 MHz |


### 2.3.5  ESD特性
| **参数** | **规格** | | **单位** | **说明** |
| :---: | :---: | --- | :---: | :---: |
| | **最小** | **最大** | |
| ESD HBM(ESDA/JEDEC JS-001-2017) | | 2000 | V | 适用核心板所有引脚 |
| ESD CDM(ESDA/JEDEC JS-002-2018) | | 500 | V | 适用核心板所有引脚 |


## 2.4  核心板接口资源
| **功能** | **数量** | **参数** |
| :---: | :---: | --- |
| LCD | 1 | 最大RGB888 24位，最高支持WXGA (1366 x 768) (60 Hz）； |
| CAMERA | 1 | 8位并行接口（DVP），最大支持5-Megapixel；  |
| SD/MMC/SDIO | ≤2 | 最高支持 UHS-I SDR104 模式的 SD 和 SDIO 卡的 1 位或 4 位传输模式规范（最大104 MB/s） |
| USB | 2 | USB 2.0 （最高支持 480 Mbps），带集成 HS USB Phy |
| SAI | ≤3 | 最高支持三个 I2S Audio； |
| SPDIF | 1 | 索尼飞利浦数字音频接口 |
| UART | ≤8 | 每个最高支持 5.0 Mbps； |
| eCSPI | ≤4 | 全双工增强同步串行接口，具有最高支持 52 Mbit/s 的数据速率。它可配置为支持主 / 从模式，有四个片选来支持多个外设。 |
| IIC | ≤4 |  |
| Ethernet | ≤2 | 10/100Mbps自适应； |
| PWM | ≤8 | 16位； |
| JTAG | 支持 |  |
| KeyPad Port | 支持 | 8*8； |
| QSPI | 1 |  |
| CAN | ≤2 | CAN 协议版本 2.0B 规范； |
| ADC | ≤10 | 两个 12 位模数转换器 (ADC)，带最高支持 10 个输入通道 |
| ISO7816-3 | ≤2 |  |
| EBI BUS | 1 | 16位并行总线 |




注：表中参数为硬件设计或CPU理论值；

## 2.5  FETMX6UL-C核心板引脚定义
### 2.5.1  FETMX6UL-C核心板引脚原理图
![](https://cdn.nlark.com/yuque/0/2024/png/45534235/1720509408520-51543db8-93f5-404b-ad17-bc7e2d152e19.png)

![](https://cdn.nlark.com/yuque/0/2024/png/45534235/1720509409078-e0eb79e0-c423-4524-a70e-cec5ad1e2992.png)

### 2.5.2  FETMX6UL- C核心板引脚功能说明
**注1：**

**    Num —— **核心板连接器引脚序号；

**    Ball —— **CPU引脚球号

**    GPIO —— **CPU引脚通用I/O口序号

**    Vol  ——** 引脚信号电平

**注2：**

**    信号名称 ——**核心板连接器网络名称

**    引脚描述 ——**核心板引脚信号名称描述

**    默认功能 ——**核心板所有引脚功能均按下表的“默认功能”作了规定，请勿修改，否则可能和出厂

                  驱动冲突。如有疑问，请及时联系我们的销售或技术支持。



**注3: “引脚描述”一栏中标明“底板勿用”的引脚是核心板使用的引脚，底板设计时不可使用**



**表1  LEFT（J302）连接器接口（奇）引脚定义**

| **Num** | **Ball** | **信号名称** | **GPIO** | **Vol** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| L_1 | G13 | UART5_RXD | gpio1.IO[31] | 3.3V | UART5接收 | IIC2_SDA |
| L_3 | F17 | UART5_TXD | gpio1.IO[30] | 3.3V | UART5发送 | IIC2_SCL |
| L_5 | G16 | UART4_RXD | gpio1.IO[29] | 3.3V | UART4接收 | IIC1_SDA |
| L_7 | G17 | UART4_TXD | gpio1.IO[28] | 3.3V | UART4发送 | IIC1_SCL |
| L_9 | H15 | UART3_CTS | gpio1.IO[26] | 3.3V | UART3清除发送 | CAN1_TX |
| L_11 | G14 | UART3_RTS | gpio1.IO[27] | 3.3V | UART3请求发送 | CAN1_RX |
| L_13 | H16 | UART3_RXD | gpio1.IO[25] | 3.3V | UART3接收 | UART3_RXD |
| L_15 | H17 | UART3_TXD | gpio1.IO[24] | 3.3V | UART3发送 | UART3_TXD |
| L_17 | — | GND | — | — | 地 | GND |
| L_19 | J15 | UART2_CTS | gpio1.IO[22] | 3.3V | UART2清除发送 | CAN2_TX |
| L_21 | H14 | UART2_RTS | gpio1.IO[23] | 3.3V | UART2请求发送 | CAN2_RX |
| L_23 | J16 | UART2_RXD | gpio1.IO[21] | 3.3V | UART2接收 | UART2_RXD |
| L_25 | J17 | UART2_TXD | gpio1.IO[20] | 3.3V | UART2发送 | UART2_TXD |
| L_27 | K15 | UART1_CTS | gpio1.IO[18] | 3.3V | UART1（调试串口）清除发送 | UART1_CTS |
| L_29 | J14 | UART1_RTS | gpio1.IO[19] | 3.3V | UART1（调试串口）请求发送 | UART1_RTS<br/>SD1­_CD |
| L_31 | K16 | UART1_RXD | gpio1.IO[17] | 3.3V | UART1（调试串口）接收 | UART1_RXD |
| L_33 | K14 | UART1_TXD | gpio1.IO[16] | 3.3V | UART1（调试串口）发送 | UART1_TXD |
| L_35 | — | GND | — | — | 地 | GND |
| L_37 | P15 | JTAG_MOD | gpio1.IO[10] | 3.3V | JTAG模式选择 | JTAG_MOD |
| L_39 | N14 | JTAG_nTRST | gpio1.IO[15] | 3.3V | JTAG测试复位 | JTAG_nTRST<br/>SAI2_TXD |
| L_41 | M14 | JTAG_TCK | gpio1.IO[14] | 3.3V | JTAG测试时钟 | JTAG_TCK<br/>SAI2_RXD |
| L_43 | P14 | JTAG_TMS | gpio1.IO[11] | 3.3V | JTAG测试模式选择 | JTAG_TMS<br/>SAI2_MCLK |
| L_45 | N16 | JTAG_TDI | gpio1.IO[13] | 3.3V | JTAG测试数据输入 | JTAG_TDI<br/>SAI2_BCLK |
| L_47 | N15 | JTAG_TDO | gpio1.IO[12] | 3.3V | JTAG测试数据输出 | JTAG_TDO<br/>SAI_SYNC |
| L_49 | — | GND | — | — | 地 | GND |
| L_51 | P16 | CLK1_N | — | — | 时钟输出— | CLK1_N |
| L_53 | P17 | CLK1_P | — | — | 时钟输出+ | CLK1_P |
| L_55 | — | GND | — | — | 地 | GND |
| L_57 | T13 | USB_OTG2_D— | — | — | USB 主口数据— | USB_OTG2_D— |
| L_59 | U13 | USB_OTG2_D+ | — | — | USB 主口数据+ | USB_OTG2_D+ |
| L_61 | U12 | USB_OTG2_VBUS | — | — | USB主口电源 | USB_OTG2_<br/>VBUS |
| L_63 | — | GND | — | — | 地 | GND |
| L_65 | U16 | nUSB_OTG1_CHD | — | — | USB充电控制端 | USB_OTG1_<br/>CHD |
| L_67 | U15 | USB_OTG1_D+ | — | — | USB OTG数据+ | USB_OTG1_D+ |
| L_69 | T15 | USB_OTG1_D- | — | — | USB OTG数据— | USB_OTG1_D— |
| L_71 | T12 | USB_OTG1_VBUS | — | — | USB OTG电源 | USB_OTG1_<br/>VBUS |
| L_73 | — | VDD_COIN_3V | — | — | RTC电池输入 | BAT1 |
| L_75 | — | GND | — | — | 地 | GND |
| L_77 | — | VSYS | — | 5V | 核心板的5V电源 | VDD_5V |
| L_79 | — | VSYS | — | 5V | 核心板的5V电源 | VDD_5V |




**表2  LEFT（J302）连接器接口（偶）引脚定义**

| **Num** | **Ball** | **信号名称** | **GPIO** | **Vol** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| L_2 | — | GND | — | — | 地 | GND |
| L_4 | D16 | ENET2_RXER | gpio2.IO[15] | 3.3V | ENET2 RMII接口帧错误 | ENET2_RXER |
| L_6 | D17 | ENET2_TX_CLK | gpio2.IO[14] | 3.3V | ENET2 RMII接口参考时钟 | ENET2_TX_CLK |
| L_8 | B15 | ENET2_TXEN | gpio2.IO[13] | 3.3V | ENET2 RMII接口发送使能 | ENET2_TXEN |
| L_10 | C16 | ENET2_RXD1 | gpio2.IO[9] | 3.3V | ENET2 RMII接口接收数据1 | ENET2_RXD1 |
| L_12 | C17 | ENET2_RXD0 | gpio2.IO[8] | 3.3V | ENET2 RMII接口接收数据0 | ENET2_RXD0 |
| L_14 | B17 | ENET2_CRS_DV | gpio2.IO[10] | 3.3V | 网口2接收数据使能 | ENET2_CRS_DV |
| L_16 | A16 | ENET2_TXD1 | gpio2.IO[12] | 3.3V | ENET2 RMII接口发送数据1 | ENET2_TXD1 |
| L_18 | A15 | ENET2_TXD0 | gpio2.IO[11] | 3.3V | ENET2 RMII接口发送数据0 | ENET2_TXD0 |
| L_20 | L16 | GPIO_7 | gpio1.IO[7] | 3.3V | 通用I/O口 | ENET2_MDC |
| L_22 | K17 | GPIO_6 | gpio1.IO[6] | 3.3V | 通用I/O口 | ENET2_MDIO |
| L_24 | — | GND | — | — | 地 | GND |
| L_26 | M17 | GPIO_5 | gpio1.IO[5] | 3.3V | 通用I/O口**（底板勿用）** | GPIO_5 |
| L_28 | M16 | GPIO_4 | gpio1.IO[4] | 3.3V | 通用I/O口 | GPIO_4 |
| L_30 | L17 | GPIO_3 | gpio1.IO[3] | 3.3V | 通用I/O口 | GPIO_3 |
| L_32 | L14 | GPIO_2 | gpio1.IO[2] | 3.3V | 通用I/O口 | GPIO_2 |
| L_34 | L15 | GPIO_1 | gpio1.IO[1] | 3.3V | 通用I/O口 | GPIO_1 |
| L_36 | K13 | GPIO_0 | gpio1.IO[0] | 3.3V | 通用I/O口 | USB_OTG1_ID |
| L_38 | M15 | GPIO_9 | gpio1.IO[9] | 3.3V | 通用I/O口 | LED3<br/>SD1_NRST |
| L_40 | N17 | GPIO_8 | gpio1.IO[8] | 3.3V | 通用I/O口 | BLT_PWM |
| L_42 | — | GND | — | — | 地 | GND |
| L_44 | R6 | SNVS_TAMPER9 | gpio5.IO[9] | 3.3V | SNVS TAMPER输入9 | LED2<br/>LCD_DISP |
| L_46 | N9 | SNVS_TAMPER8 | gpio5.IO[8] | 3.3V | SNVS TAMPER输入8 | SHIFT_NOE |
| L_48 | N10 | SNVS_TAMPER7 | gpio5.IO[7] | 3.3V | SNVS TAMPER输入7 | SHIFT_STCP |
| L_50 | N11 | SNVS_TAMPER6 | gpio5.IO[6] | 3.3V | SNVS TAMPER输入6 | ENET2_NINT |
| L_52 | N8 | SNVS_TAMPER5 | gpio5.IO[5] | 3.3V | SNVS TAMPER输入5 | ENET1_NINT |
| L_54 | P9 | SNVS_TAMPER4 | gpio5.IO[4] | 3.3V | SNVS TAMPER输入4 | AUD_INT |
| L_56 | P10 | SNVS_TAMPER3 | gpio5.IO[3] | 3.3V | SNVS TAMPER输入3 | SNVS_TAMPER3 |
| L_58 | — | GND | | 3.3V | 地 | GND |
| L_60 | P11 | SNVS_TAMPER2 | gpio5.IO[2] | 3.3V | SNVS TAMPER输入2 | PERI_PWREN |
| L_62 | R9 | SNVS_TAMPER1 | gpio5.IO[1] | 3.3V | SNVS TAMPER输入1 | TP_INT |
| L_64 | R10 | SNVS_TAMPER0 | gpio5.IO[0] | 3.3V | SNVS TAMPER输入0 | ACC_INT |
| L_66 | U10 | BOOT_MODE1 | gpio5.IO[11] | 3.3V | 启动模式选择1脚 | SHIFT_SHCP<br/>BOOT_MODE1 |
| L_68 | T10 | BOOT_MODE0 | gpio5.IO[10] | 3.3V | 启动模式选择1脚 | SHIFT_SDI<br/>BOOT_MODE0 |
| L_70 | R8 | ONOFF | — | — | 开关机键，不用可以悬空 | ONOFF |
| L_72 | P8 | POR_B | — | — | i.MX6UL上电复位引脚，<br/>不用可以悬空 | POR_B |
| L_74 | — | MX6_POR_B | — | — | 核心板断电复位，低电平有效 | MX6_POR_B |
| L_76 | T9 | PMIC_ON_REQ | — | — | 控制底板GEN_5V和GEN_3.3V输出高电平有效 | PMIC_ON_REQ |
| L_78 | U9 | PMIC_STBY_REQ | — | — | PMIC Standby信号，用于动态调整VDD_SOC_IN电压<br/>**（底板勿用）** | PMIC_STBY_<br/>REQ |
| L_80 | — | GND | — | — | 地 | GND |


**表3  RIGHT（J303）连接器接口（奇）引脚定义**

| **Num** | **Ball** | **信号名称** | **GPIO** | **Vol** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| R_1 | D9 | LCD_HSYNC | gpio3.IO[2] | 3.3V | RGB接口水平同步信号 | LCD_HSYNC |
| R_3 | C9 | LCD_VSYNC | gpio3.IO[3] | 3.3V | RGB接口垂直同步信号 | LCD_VSYNC |
| R_5 | B8 | LCD_DE | gpio3.IO[1] | 3.3V | RGB接口数据使能信号 | LCD_DE |
| R_7 | — | GND | **—** | 0V | 地 | GND |
| R_9 | A8 | LCD_PCLK | gpio3.IO[0] | 3.3V | RGB接口像素时钟信号 | LCD_PCLK |
| R_11 | E9 | LCD_RST | gpio3.IO[4] | 3.3V | RGB接口复位信号<br/>（**默认不可用**） | LCD_RST |
| R_13 | D15 | ENET1_RXER | gpio2.IO[7] | 3.3V | ENET1 RMII接口帧错误信号 | ENET1_RXER |
| R_15 | F14 | ENET1_TX_CLK | gpio2.IO[6] | 3.3V | ENET1 RMII接口参考时钟信号 | ENET1_TX_CLK |
| R_17 | F15 | ENET1_TXEN | gpio2.IO[5] | 3.3V | ENET1 RMII接口发送使能信号 | ENET1_TXEN |
| R_19 | E14 | ENET1_TXD1 | gpio2.IO[4] | 3.3V | ENET1 RMII接口发送数据信号1 | ENET1_TXD1 |
| R_21 | E15 | ENET1_TXD0 | gpio2.IO[3] | 3.3V | ENET1 RMII接口发送数据信号0 | ENET1_TXD0 |
| R_23 | E16 | ENET1_CRS_DV | gpio2.IO[2] | 3.3V | ENET1 RMII接口RX_EN、CRS信号 | ENET1_CRS_DV |
| R_25 | E17 | ENET1_RXD1 | gpio2.IO[1] | 3.3V | ENET1 RMII接口接收数据信号1 | ENET1_RXD1 |
| R_27 | F16 | ENET1_RXD0 | gpio2. .IO[0] | 3.3V | ENET1 RMII接口接收数据信号0 | ENET1_RXD0 |
| R_29 | — | GND | **—** | **—** | 地 | GND |
| R_31 | A5 | NAND_DATA7 | gpio4.IO[9] | 3.3V | NAND接口数据信号7<br/>**（底板勿用）** | NAND_DATA7 |
| R_33 | A6 | NAND_DATA6 | gpio4.IO[8] | 3.3V | NAND接口数据信号6<br/>**（底板勿用）** | NAND_DATA6 |
| R_35 | B6 | NAND_DATA5 | gpio4.IO[7] | 3.3V | NAND接口数据信号5<br/>**（底板勿用）** | NAND_DATA5 |
| R_37 | C6 | NAND_DATA4 | gpio4.IO[6] | 3.3V | NAND接口数据信号4<br/>**（底板勿用）** | NAND_DATA4 |
| R_39 | D6 | NAND_DATA3 | gpio4.IO[5] | 3.3V | NAND接口数据信号3<br/>**（底板勿用）** | NAND_DATA3 |
| R_41 | A7 | NAND_DATA2 | gpio4.IO[4] | 3.3V | NAND接口数据信号2<br/>**（底板勿用）** | NAND_DATA2 |
| R_43 | B7 | NAND_DATA1 | gpio4.IO[3] | 3.3V | NAND接口数据信号1<br/>**（底板勿用）** | NAND_DATA1 |
| R_45 | D7 | NAND_DATA0 | gpio4.IO[2] | 3.3V | NAND接口数据信号0<br/>**（底板勿用）** | NAND_DATA0 |
| R_47 | C8 | NAND_nWE | gpio4.IO[1] | 3.3V | NAND接口写控制信号<br/>**（底板勿用）** | NAND_nWE |
| R_49 | D8 | NAND_nRE | gpio4.IO[0] | 3.3V | NAND接口读控制信号<br/>**（底板勿用）** | NAND_nRE |
| R_51 | E5 | CSI_PIXCLK | gpio4.IO[18] | 3.3V | 数字摄像头的像素时钟输入 | CSI_PIXCLK |
| R_53 | F3 | CSI_HSYNC | gpio4.IO[20] | 3.3V | 数字摄像头的行同步信号输入 | CSI_HSYNC |
| R_55 | F5 | CSI_MCLK | gpio4.IO[17] | 2.7V | 数字摄像头的主时钟输入 | CSI_MCLK |
| R_57 | F2 | CSI_VSYNC | gpio4.IO[19] | 2.7V | 数字摄像头的场同步信号输入 | CSI_VSYNC |
| R_59 | — | GND | **—** | **—** | 地 | GND |
| R_61 | E4 | CSI_DAT0 | gpio4.IO[21] | 2.7V | 8bit数字摄像头数据0输入 | CSI_DAT0 |
| R_63 | E3 | CSI_DAT1 | gpio4.IO[22] | 2.7V | 8bit数字摄像头数据1输入 | CSI_DAT1 |
| R_65 | E2 | CSI_DAT2 | gpio4.IO[23] | 2.7V | 8bit数字摄像头数据2输入 | CSI_DAT2 |
| R_67 | E1 | CSI_DAT3 | gpio4.IO[24] | 2.7V | 8bit数字摄像头数据3输入 | CSI_DAT3 |
| R_69 | D4 | CSI_DAT4 | gpio4.IO[25] | 2.7V | 8bit数字摄像头数据4输入 | CSI_DAT4 |
| R_71 | D3 | CSI_DAT5 | gpio4.IO[26] | 2.7V | 8bit数字摄像头数据5输入 | CSI_DAT5 |
| R_73 | D2 | CSI_DAT6 | gpio4.IO[27] | 2.7V | 8bit数字摄像头数据6输入 | CSI_DAT6 |
| R_75 | D1 | CSI_DAT7 | gpio4.IO[28] | 2.7V | 8bit数字摄像头数据7输入 | CSI_DAT7 |
| R_77 | — | GND | **—** | **—** | 地 | GND |
| R_79 | — | NVCC_CSI_IN | **—** | **—** | CPU内部摄像头部分的电源 | NVCC_CSI_IN |


**表4  RIGHT（J303）连接器接口（偶）引脚定义**

| **Num** | **Ball** | **信号名称** | **GPIO** | **Vol** | **引脚描述** | **默认功能** |
| :---: | :---: | :---: | :---: | :---: | --- | :---: |
| R_2 | B16 | LCD_DATA23 | gpio3.IO[28] | 3.3V | 红色数据位7（高） | LCD_DATA23 |
| R_4 | A14 | LCD_DATA22 | gpio3.IO[27] | 3.3V | 红色数据位6 | LCD_DATA22 |
| R_6 | B14 | LCD_DATA21 | gpio3.IO[26] | 3.3V | 红色数据位5 | LCD_DATA21 |
| R_8 | C14 | LCD_DATA20 | gpio3.IO[25] | 3.3V | 红色数据位4 | LCD_DATA20 |
| R_10 | D14 | LCD_DATA19 | gpio3.IO[24] | 3.3V | 红色数据位3 | LCD_DATA19 |
| R_12 | A13 | LCD_DATA18 | gpio3.IO[23] | 3.3V | 红色数据位2 | LCD_DATA18 |
| R_14 | B13 | LCD_DATA17 | gpio3.IO[22] | 3.3V | 红色数据位1 | LCD_DATA17 |
| R_16 | C13 | LCD_DATA16 | gpio3.IO[21] | 3.3V | 红色数据位0（低） | LCD_DATA16 |
| R_18 | — | GND | **—** | 0V | 地 | GND |
| R_20 | D13 | LCD_DATA15 | gpio2.IO[4] | 3.3V | 绿色数据位7（高） | LCD_DATA15 |
| R_22 | A12 | LCD_DATA14 | gpio3.IO[19] | 3.3V | 绿色数据位6 | LCD_DATA14 |
| R_24 | B12 | LCD_DATA13 | gpio3.IO[18] | 3.3V | 绿色数据位5 | LCD_DATA13 |
| R_26 | C12 | LCD_DATA12 | gpio3.IO[17] | 3.3V | 绿色数据位4 | LCD_DATA12 |
| R_28 | D12 | LCD_DATA11 | gpio3.IO[16] | 3.3V | 绿色数据位3 | LCD_DATA11 |
| R_30 | E12 | LCD_DATA10 | gpio3.IO[15] | 3.3V | 绿色数据位2 | LCD_DATA10 |
| R_32 | A11 | LCD_DATA9 | gpio3.IO[14] | 3.3V | 绿色数据位1 | LCD_DATA9 |
| R_34 | B11 | LCD_DATA8 | gpio3.IO[13] | 3.3V | 绿色数据位0（低） | LCD_DATA8 |
| R_36 | — | GND | — | — | 地 | GND |
| R_38 | D11 | LCD_DATA7 | gpio3.IO[12] | 3.3V | 蓝色数据位7(高) | LCD_DATA7 |
| R_40 | A10 | LCD_DATA6 | gpio3.IO[11] | 3.3V | 蓝色数据位6 | LCD_DATA6 |
| R_42 | B10 | LCD_DATA5 | gpio3.IO[10] | 3.3V | 蓝色数据位5 | LCD_DATA5 |
| R_44 | C10 | LCD_DATA4 | gpio3.IO[9] | 3.3V | 蓝色数据位4 | LCD_DATA4 |
| R_46 | D10 | LCD_DATA3 | gpio3.IO[8] | 3.3V | 蓝色数据位3 | LCD_DATA3 |
| R_48 | E10 | LCD_DATA2 | gpio3.IO[7] | 3.3V | 蓝色数据位2 | LCD_DATA2 |
| R_50 | A9 | LCD_DATA1 | gpio3.IO[6] | 3.3V | 蓝色数据位1 | LCD_DATA1 |
| R_52 | B9 | LCD_DATA0 | gpio3.IO[5] | 3.3V | 蓝色数据位0（低） | LCD_DATA0 |
| R_54 | — | GND | — | — | 地 | GND |
| R_56 | E6 | NAND_DQS | gpio4.IO[16] | 3.3V | NAND模式选择 | NAND_DQS |
| R_58 | D5 | NAND_nWP | gpio4.IO[11] | 3.3V | NAND接口写保护信号<br/>（**Nand版勿用**） | NAND_nWP |
| R_60 | B4 | NAND_ALE | gpio4.IO[10] | 3.3V | NAND接口地址锁存信号<br/>（**Nand版勿用**） | NAND_ALE |
| R_62 | A4 | NAND_CLE | gpio4.IO[15] | 3.3V | NAND接口命令锁存信号<br/>（**Nand版勿用**） | NAND_CLE |
| R_64 | B5 | NAND_nCE1 | gpio4.IO[14] | 3.3V | NAND接口片选信号1 | NAND_nCE1 |
| R_66 | C5 | NAND_nCE0 | gpio4.IO[13] | 3.3V | NAND接口片选信号0<br/>（**Nand版勿用**） | NAND_nCE0 |
| R_68 | A3 | NAND_nREADY | gpio4.IO[12] | 3.3V | NAND接口忙信号<br/>（**Nand版勿用**） | NAND_nREADY |
| R_70 | B3 | SD1_DATA0 | gpio2.IO[18] | 3.3V | SD/MMC1接口数据信号0 | SD1_DATA0 |
| R_72 | B2 | SD1_DATA1 | gpio2.IO[19] | 3.3V | SD/MMC1接口数据信号1 | SD1_DATA1 |
| R_74 | C1 | SD1_CLK | gpio2.IO[17] | 3.3V | SD/MMC1接口时钟信号 | SD1_CLK |
| R_76 | C2 | SD1_CMD | gpio2.IO[16] | 3.3V | SD/MMC1接口命令信号 | SD1_CMD |
| R_78 | A2 | SD1_DATA3 | gpio2.IO[21] | 3.3V | SD/MMC1接口数据信号3 | SD1_DATA3 |
| R_80 | B1 | SD1_DATA2 | gpio2.IO[20] | 3.3V | SD/MMC1接口数据信号2 | SD1_DATA2 |




## 2.6  核心板硬件设计说明
   FETMX6UL-C核心板已经将电源、复位监控电路、存储电路集成于一个小巧的模块上，所需的外部电路非常简洁,构成一个最小系统只需要 5V 电源、复位按键、启动配置即可运行,如下图所示:

最小系统原理图可以参见附录四。不过一般情况下，除最小系统外建议连接上一些外部设备，例如调试串口，否则用户无法判断系统是否启动。做好这些后，再在此基础上根据飞凌提供的核心板默认接口定义来添加用户需要的功能。



核心板外围电路的设计可参见第三章的3.5节“OKMX6UL-C底板说明”。





