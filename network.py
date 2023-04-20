import sys

def main():
    ip_address, cidr = str(sys.argv[1]).split("/")[0], int(sys.argv[1].split("/")[1])
    if (cidr<1)or(cidr>32):
        print("This value must be interval 1 - 32")
        raise IndexError
    ip_class = get_ip_class(ip_address=ip_address)
    subnet_mask = get_subnetmask(cidr=cidr)
    print("Entered Ip Address's Class: {}".format(ip_class))
    print("Entered Ip Address's Subnet Mask: {}".format(subnet_mask))
    
def get_ip_class(ip_address:str):
    seek_okted = int(ip_address.split(".")[0])
    if (seek_okted >= 1) or (seek_okted <= 127):
        return "A Class"
    elif (seek_okted >= 128) or (seek_okted <= 191):
        return "B Class"
    elif (seek_okted >= 192) or (seek_okted <= 223):
        return "C Class"
    elif (seek_okted >= 224) or (seek_okted <= 239):
        return "D Class"
    elif (seek_okted >= 240) or (seek_okted <= 255):
        return "E Class"
    else:
        return "Invalid IP Address!"  

def get_subnetmask(cidr:int):
    binary_str, subnet_mask = "", ""
    for _ in range(cidr):
        binary_str += "1"
    binary_str = binary_str.zfill(32)[::-1]
    binary_list = list(map(''.join, zip(*[iter(binary_str)]*8)))
    for okted in binary_list:
        okted = int(okted, 2)
        subnet_mask += str(okted)+"."
    return subnet_mask[:-1]

if __name__ == '__main__':
    main()
