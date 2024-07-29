import pyautogui
import time

def send_can_message_via_cantest(can_id, data):
    # Convert CAN ID and data to hex strings
    can_id_str = f"{can_id:08X}"
    data_str = ' '.join(f"{byte:02X}" for byte in data)

    # Activate CANTest window (assuming it's already open)
    pyautogui.getWindowsWithTitle("CANTest")[0].activate()

   
    # Enter Data
    pyautogui.click(1942, 1320)  # Adjust coordinates to the Data input box
    pyautogui.press('delete', presses=30, interval=0.001) 
    pyautogui.typewrite(data_str)
    
    # Click Send button
    pyautogui.click(2200, 1320)  # Adjust coordinates to the Send button


def main():
    # Danh sách các bản tin CAN cần gửi
    messages = [
        #1.
        [0x07, 0x01, 0x60], # start Jig test
                        
        #I.Test GSM/GPS
        2. AT CMD
        [0x07, 0x10, 0x0a, 0x62, 0x06, 0x05, 0x09, 0x41], # send AT&F
        [0x07, 0x21, 0x54, 0x26, 0x46, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],

        [0x07, 0x10, 0x08, 0x62, 0x06, 0x05, 0x09, 0x41], # send AT
        [0x07, 0x21, 0x54, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],

        [0x07, 0x10, 0x09, 0x62, 0x06, 0x05, 0x0b, 0x41],  # ATE
        [0x07, 0x21, 0x54, 0x45, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],

        [0x07, 0x10, 0x0A, 0x41, 0x54, 0x2B, 0x43, 0x46],  # AT+CFU=0
        [0x07, 0x21, 0x55, 0x4E, 0x3D, 0x30, 0x0D, 0x0A],        
        [0x07, 0x30, 0x55, 0x01],                  
            
        #3.Init GPS
        [0x07, 0x10, 0x0f, 0x62, 0x06, 0x05, 0x18, 0x41],  # AT+QGPS=1
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x47, 0x50, 0x53],
        [0x07, 0x22, 0x3D, 0x31, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],

        [0x07, 0x10, 0x1c, 0x62, 0x06, 0x05, 0x18, 0x41],  # AT+QGPSCFG="nmeasrc",1
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x47, 0x50, 0x53],
        [0x07, 0x22, 0x43, 0x46, 0x47, 0x3d, 0x22, 0x6e],
        [0x07, 0x23, 0x6d, 0x65, 0x61, 0x73, 0x72, 0x63],
        [0x07, 0x24, 0x22, 0x2c, 0x31, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],

        #4.read GPS cmd
        [0x07, 0x10, 0x17, 0x62, 0x06, 0x05, 0x13, 0x41],  # AT+QGPSGNMEA="GSV"
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x47, 0x50, 0x53],
        [0x07, 0x22, 0x47, 0x4e, 0x4d, 0x45, 0x41, 0x3d],
        [0x07, 0x23, 0x22, 0x47, 0x53, 0x56, 0x22, 0x0d],
        [0x07, 0x30, 0x55, 0x01],

        #II. Test SCU LTE Band1
        [0x07, 0x10, 0x16, 0x62, 0x06, 0x05, 0x12, 0x41],  # AT+QRFTESTMODE=1
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x4d, 0x4f, 0x44],
        [0x07, 0x23, 0x45, 0x3d, 0x31, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],    

        [0x07, 0x10, 0x2c, 0x62, 0x06, 0x05, 0x28, 0x41],  # AT+QRFTEST="LTE BAND1",18300,"ON",23,2
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x3d, 0x22, 0x4c],
        [0x07, 0x23, 0x54, 0x45, 0x20, 0x42, 0x41, 0x4e],
        [0x07, 0x24, 0x44, 0x31, 0x22, 0x2c, 0x31, 0x38],
        [0x07, 0x25, 0x33, 0x30, 0x30, 0x2c, 0x22, 0x4f],
        [0x07, 0x26, 0x4e, 0x22, 0x2c, 0x32, 0x33, 0x2c],
        [0x07, 0x27, 0x32, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],  
        #test done
        [0x07, 0x10, 0x2d, 0x62, 0x06, 0x05, 0x28, 0x41],  # AT+QRFTEST="LTE BAND1",18300,"OFF",23,2
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x3d, 0x22, 0x4c],
        [0x07, 0x23, 0x54, 0x45, 0x20, 0x42, 0x41, 0x4e],
        [0x07, 0x24, 0x44, 0x31, 0x22, 0x2c, 0x31, 0x38],  
        [0x07, 0x25, 0x33, 0x30, 0x30, 0x2c, 0x22, 0x4f],  
        [0x07, 0x26, 0x46, 0x46, 0x22, 0x2c, 0x32, 0x33],  
        [0x07, 0x27, 0x2c, 0x32, 0x0d, 0x0a],               
        [0x07, 0x30, 0x55, 0x01],    

        #Test LTE band 3
        [0x07, 0x10, 0x2c, 0x62, 0x06, 0x05, 0x28, 0x41],  # AT+QRFTEST="LTE BAND3",19575,"ON",23,2
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x3d, 0x22, 0x4c],
        [0x07, 0x23, 0x54, 0x45, 0x20, 0x42, 0x41, 0x4e],
        [0x07, 0x24, 0x44, 0x33, 0x22, 0x2c, 0x31, 0x39],  
        [0x07, 0x25, 0x35, 0x37, 0x35, 0x2c, 0x22, 0x4f],  
        [0x07, 0x26, 0x4e, 0x22, 0x2c, 0x32, 0x33, 0x2c], 
        [0x07, 0x27, 0x32, 0x0d, 0x0a],                    
        [0x07, 0x30, 0x55, 0x01],                                              
        #test done
        [0x07, 0x10, 0x2d, 0x62, 0x06, 0x05, 0x28, 0x41],  # AT+QRFTEST="LTE BAND3",19575,"OFF",23,2
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x3d, 0x22, 0x4c],
        [0x07, 0x23, 0x54, 0x45, 0x20, 0x42, 0x41, 0x4e],
        [0x07, 0x24, 0x44, 0x33, 0x22, 0x2c, 0x31, 0x39],  
        [0x07, 0x25, 0x35, 0x37, 0x35, 0x2c, 0x22, 0x4f],  
        [0x07, 0x26, 0x46, 0x46, 0x22, 0x2c, 0x32, 0x33], 
        [0x07, 0x27, 0x2c, 0x32, 0x0d, 0x0a],              
        [0x07, 0x30, 0x55, 0x01],                         

        #Exit FTM mode
        [0x07, 0x10, 0x16, 0x62, 0x06, 0x05, 0x12, 0x41],  # AT+QRFTESTMODE=0
        [0x07, 0x21, 0x54, 0x2b, 0x51, 0x52, 0x46, 0x54],
        [0x07, 0x22, 0x45, 0x53, 0x54, 0x4d, 0x4f, 0x44],
        [0x07, 0x23, 0x45, 0x3d, 0x30, 0x0d, 0x0a],
        [0x07, 0x30, 0x55, 0x01],                      
    ]
    
    # ID CAN
    can_id = 0x0A
    
    # Gửi từng bản tin
    for index, data in enumerate(messages):
        send_can_message_via_cantest(can_id, data)
        if data == [0x07, 0x30, 0x55, 0x01]:  # Thêm delay sau mỗi bản tin này
            time.sleep(3)        
        # if index in {1, 2}:
        #     time.sleep(2) 

if __name__ == "__main__":
    main()
