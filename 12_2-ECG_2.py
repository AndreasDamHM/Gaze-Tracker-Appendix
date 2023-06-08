import csv
"""Hard reset AFE4960"""
reset_AFE_GUI()

"""Lead construction"""
AFE.component.segment.AFE4960.AFE4960_global.SW_ECG_INP_ECG					= 2
AFE.component.segment.AFE4960.AFE4960_global.SW_ECG_INM_ECG					= 8
AFE.component.segment.AFE4960.AFE4960_global.SW_BIOZ_RXP					= 5
AFE.component.segment.AFE4960.AFE4960_global.SW_BIOZ_RXM					= 6
AFE.component.segment.AFE4960.AFE4960_global.SW_BIOZ_TXP					= 0
AFE.component.segment.AFE4960.AFE4960_global.SW_BIOZ_TXM					= 0
AFE.component.segment.AFE4960.AFE4960_global.SW_RLD							= 1

"""Signal Acquisition configuration"""
AFE.component.segment.AFE4960.AFE4960_global.COUNT_RAC						= 96
AFE.component.segment.AFE4960.AFE4960_global.REG_NUM_TS						= 1
AFE.component.segment.AFE4960.AFE4960_global.REG_NUM_ESAW					= 0
AFE.component.segment.AFE4960.AFE4960_global.REG_NUM_BSAW					= 0
AFE.component.segment.AFE4960.AFE4960_global.CONFIG_TS0						= 1
AFE.component.segment.AFE4960.AFE4960_global.CONFIG_TS1						= 3

"""Clocking configuration"""
AFE.component.segment.AFE4960.AFE4960_global.SEL2_CLK_TE					= 0
AFE.component.segment.AFE4960.AFE4960_global.OSCL_DIS						= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_OSCL_SYNC					= 1
AFE.component.segment.AFE4960.AFE4960_global.DIS_DYN_PDN_OSCH 				= 0
AFE.component.segment.AFE4960.AFE4960_global.SEL1_CLK_BIOZ					= 0
AFE.component.segment.AFE4960.AFE4960_global.SEL2_CLK_BIOZ					= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_PLL							= 0
AFE.component.segment.AFE4960.AFE4960_global.SEL2_CLK_RAC					= 0
AFE.component.segment.AFE4960.AFE4960_global.DIV_TE_RAC_OUT_EN				= 0
AFE.component.segment.AFE4960.AFE4960_global.DIV_OUT_BIOZ					= 0

"""Signal chain configuration"""
AFE.component.segment.AFE4960.AFE4960_global.ECG_INA_GAIN					= 5
AFE.component.segment.AFE4960.AFE4960_global.EN_DEC_ECG						= 1
AFE.component.segment.AFE4960.AFE4960_global.ECG_DEC_FACTOR					= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_ECG2						= 1
AFE.component.segment.AFE4960.AFE4960_global.SEL_IN_BIOZ_RX					= 1
AFE.component.segment.AFE4960.AFE4960_global.RECONFIGURE_BIOZ_LPF 			= 1
AFE.component.segment.AFE4960.AFE4960_global.EN_RLD_LOOP_ECG2				= 0
AFE.component.segment.AFE4960.AFE4960_global.BIOZ_LPF_BW					= 2
AFE.component.segment.AFE4960.AFE4960_global.SEL_CHPF1_BIOZ					= 0
AFE.component.segment.AFE4960.AFE4960_global.SEL_RHPF1_BIOZ					= 2
AFE.component.segment.AFE4960.AFE4960_global.BIOZ_INA_GAIN					= 3
AFE.component.segment.AFE4960.AFE4960_global.PROCESS_BSAW					= 3
AFE.component.segment.AFE4960.AFE4960_global.EN_DEC_BIOZ					= 1
AFE.component.segment.AFE4960.AFE4960_global.BIOZ_DEC_FACTOR				= 0
AFE.component.segment.AFE4960.AFE4960_global.ACQ_MODE_SEL					= 74
AFE.component.segment.AFE4960.AFE4960_global.EN_ECG_RX						= 1
AFE.component.segment.AFE4960.AFE4960_global.PDN_ECG_INA					= 0
AFE.component.segment.AFE4960.AFE4960_global.PDN_ECG_RLD					= 0
AFE.component.segment.AFE4960.AFE4960_global.PDN_ADC						= 0
AFE.component.segment.AFE4960.AFE4960_global.PDN_OSCH						= 0
AFE.component.segment.AFE4960.AFE4960_global.PDN_ILEAD						= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_BIOZ_RX						= 1
AFE.component.segment.AFE4960.AFE4960_global.EN_BIOZ_TX						= 1
AFE.component.segment.AFE4960.AFE4960_global.DIS_ACTIVE_BIOZ_TX				= 1
AFE.component.segment.AFE4960.AFE4960_global.DIS_BUF_PDN_ON_ADC				= 1
AFE.component.segment.AFE4960.AFE4960_global.DIS_PD_REFSYS					= 1
AFE.component.segment.AFE4960.AFE4960_global.DIS_PD_VCM						= 1
AFE.component.segment.AFE4960.AFE4960_global.PDNAFE							= 0
AFE.component.segment.AFE4960.AFE4960_global.PDN_BG_IN_DEEP_SLEEP			= 0
AFE.component.segment.AFE4960.AFE4960_global.DIS_CHOP_INA1					= 0
AFE.component.segment.AFE4960.AFE4960_global.DIS_CHOP_INA2					= 0
AFE.component.segment.AFE4960.AFE4960_global.TIMER_ENABLE					= 1
AFE.component.segment.AFE4960.AFE4960_global.RAC_COUNTER_ENABLE				= 1
AFE.component.segment.AFE4960.AFE4960_global.FIFO_EN						= 1
AFE.component.segment.AFE4960.AFE4960_global.REG_WM_FIFO					= 0 


"""Interrupt configuration"""
AFE.component.segment.AFE4960.AFE4960_global.INT_MUX_ADC_RDY_1				= 2
AFE.component.segment.AFE4960.AFE4960_global.EN_GPIO2_OUT					= 1
AFE.component.segment.AFE4960.AFE4960_global.INT_MUX_GPIO2_2				= 1
AFE.component.segment.AFE4960.AFE4960_global.MASK_DC_LEAD_DET				= 0
AFE.component.segment.AFE4960.AFE4960_global.MASK_AC_LEAD_ON				= 1
AFE.component.segment.AFE4960.AFE4960_global.MASK_AC_LEAD_OFF				= 1
AFE.component.segment.AFE4960.AFE4960_global.MASK_ADC_FIFO_RDY				= 1  
AFE.component.segment.AFE4960.AFE4960_global.MASK_PACE_VALID_INT			= 0
AFE.component.segment.AFE4960.AFE4960_global.MASK_DISABLE1					= 1
AFE.component.segment.AFE4960.AFE4960_global.MASK_DISABLE2					= 1

"""Pace pulse detect configuration"""
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE						= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_SET_HIGH_2				= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_SET_HIGH_1				= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_SET_HIGH_0				= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_CONFIG_REG1 				= 995684
AFE.component.segment.AFE4960.AFE4960_global.PACE_CONFIG_REG2				= 1048256
AFE.component.segment.AFE4960.AFE4960_global.PACE_DIS_RESP_REJECT			= 1
AFE.component.segment.AFE4960.AFE4960_global.SEL_CLK_PACE					= 0
AFE.component.segment.AFE4960.AFE4960_global.WIDTH_PACE_MIN					= 4
AFE.component.segment.AFE4960.AFE4960_global.WIDTH_PACE_MAX					= 135
AFE.component.segment.AFE4960.AFE4960_global.PACE_OBS_EXTEND				= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_VALID_COMPLETE			= 1
AFE.component.segment.AFE4960.AFE4960_global.PACE_REF1_H					= 2
AFE.component.segment.AFE4960.AFE4960_global.PACE_REF1_L					= 2
AFE.component.segment.AFE4960.AFE4960_global.PACE_FIFO_DATA_CTRL			= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_WINDOW_ADC_RDY			= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_WINDOW_GPIO2			= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_VALID_TAG				= 1
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_OVERLAP_TAG			= 0
AFE.component.segment.AFE4960.AFE4960_global.USE_PACE_OVERLAP_TAG			= 0
AFE.component.segment.AFE4960.AFE4960_global.USE_BOTH_PACE_TAGS				= 0
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_TAG_ECG_CH1			= 1
AFE.component.segment.AFE4960.AFE4960_global.EN_PACE_TAG_ECG_CH2			= 1 

"""DC Lead Detection Configuration """
AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS1_ECGP 		= 1
AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS1_LEAD_BIAS 	= 1
AFE.component.segment.AFE4960.AFE4960_global.POL_RBIAS1_LEAD_BIAS 	= 0

AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS2_ECGM 		= 1
AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS2_LEAD_BIAS 	= 1
AFE.component.segment.AFE4960.AFE4960_global.POL_RBIAS2_LEAD_BIAS 	= 1

AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS3_ECG1 		= 3
AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS3_LEAD_BIAS 	= 1
AFE.component.segment.AFE4960.AFE4960_global.POL_RBIAS3_LEAD_BIAS 	= 0

AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS4_ECG2 		= 3
AFE.component.segment.AFE4960.AFE4960_global.SW_RBIAS4_LEAD_BIAS 	= 0
AFE.component.segment.AFE4960.AFE4960_global.POL_RBIAS4_LEAD_BIAS 	= 0

AFE.component.segment.AFE4960.AFE4960_global.SEL_RBIAS_CH1 			= 0
AFE.component.segment.AFE4960.AFE4960_global.SEL_RBIAS_CH2 			= 0
AFE.component.segment.AFE4960.AFE4960_global.LEAD_DET_THR_L 		= 3
AFE.component.segment.AFE4960.AFE4960_global.LEAD_DET_THR_H 		= 3
AFE.component.segment.AFE4960.AFE4960_global.EN_COMP_ANA 			= 1
AFE.component.segment.AFE4960.AFE4960_global.LEAD_DET_MODULE_CLK_EN = 1
AFE.component.segment.AFE4960.AFE4960_global.LEAD_DET_WIDTH 		= 100




"""Software requirements"""
"""Update the sequence of data in FIFO"""
FIFO_ORDER																	= np.array(["ECG_CH1","ECG_CH2"])
regCapture._controller.updateFiFoOrder(FIFO_ORDER)



"""Update the data rate"""
dataToAddDict																= {"KEY":"ECG_CH1", 		"DATA_RATE":"682.666666667"}
addData(dataToAddDict)
dataToAddDict																= {"KEY":"ECG_CH1_RAW", 	"DATA_RATE":"682.666666667"}
addData(dataToAddDict)
dataToAddDict																= {"KEY":"ECG_CH2", 		"DATA_RATE":"682.666666667"}
addData(dataToAddDict)
dataToAddDict																= {"KEY":"ECG_CH2_RAW", 	"DATA_RATE":"682.666666667"}
addData(dataToAddDict)

"""Additional registers to read"""
dataToAddDict																= {"KEY":"REG_BC", 			"DATA_RATE":"682.666666667"}
addData(dataToAddDict)

"""Mandatory register to read"""
dataToAddDict																= {"KEY":"REG_6D", 			"DATA_RATE":"682.666666667"}
addData(dataToAddDict)

dataToAddDict																= {"KEY":"REG_BD", 			"DATA_RATE":"682.666666667"}
addData(dataToAddDict)

"""Add data for plotting"""
addDataToPlot("'ECG_CH1'", 					1, filter="Enable", color=color['Red'])
addDataToPlot("'ECG_CH2'", 					2, filter="Enable", color=color['Green'])
"""addDataToPlot("'ECG_CH1'", 					3, filter="Disable", color=color['Red'])
addDataToPlot("PACE_STATUS('AFE_REG_BC')",	4, filter="Disable", color=color['Green'])
"""

"""For capturing and exporting"""
workSpaceWindow.startCapture()
ECG_Data = 0
delay(0.2)
n = 0.0
regCapture._controller.capturedDataDict['ECG_CH1'] = np.delete(regCapture._controller.capturedDataDict['ECG_CH1'],np.s_[:],0)
regCapture._controller.capturedDataDict['ECG_CH2'] = np.delete(regCapture._controller.capturedDataDict['ECG_CH2'],np.s_[:],0)
delay(0.0001)

with open("C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/ECG_CH1Vert.csv", 'a') as file:
	file.truncate(0)
with open("C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/ECG_CH2.csv", 'a') as file:
	file.truncate(0)

def ExportData(KEY):
	
	ECG_Data = regCapture._controller.capturedDataDict[KEY] #read the new values
	regCapture._controller.capturedDataDict[KEY] = np.delete(regCapture._controller.capturedDataDict[KEY],np.s_[:],0) #clear the list for new values
	print(ECG_Data.size)
	
	
	if ECG_Data.size == 0: # make sure data was extracted
		n = 1
		return n
		
	# write to the csv file
	with open("C:/Users/andre/OneDrive/Dokumenter/Texas Instruments/Bio-Sensing/projects/AFE4960EVM/GUI/" + KEY + ".csv", 'a') as file:
		writer = csv.writer(file, delimiter = ';')
		writer.writerow(ECG_Data)

k = 0

while True:
	delay(0.0008)
	n = ExportData('ECG_CH1')
	n = ExportData('ECG_CH2')
	print(n) #n hstops the loop if the data stream stops
	if n == 1:
		k += 1
	else:
		k = 0 
	if k == 10:
		break
		

workSpaceWindow.stopCapture()

MODE	= "2-ECG"
