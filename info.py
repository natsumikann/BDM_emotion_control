import get_temperature
import get_moisture

def init():
    f = open("info.txt", "w")
    data = []
    data.append(get_temperature.get_value())
    data.append(get_moisture.get_value())
    data.append(20)
    f.write(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    f.close()

def change_temperature():
    f = open("info.txt", "r")
    data = f.readline().replace('\n', '').split(' ')
    f.close()
    data[0] = get_temperature.get_value()
    f = open("info.txt", "w")
    f.write(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    f.close()

def change_moisture():
    f = open("info.txt", "r")
    data = f.readline().replace('\n', '').split(' ')
    f.close()
    data[1] = get_moisture.get_value()
    f = open("info.txt", "w")
    f.write(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    f.close()

def add_friendship(diff):
    f = open("info.txt", "r")
    data = f.readline().replace('\n', '').split(' ')
    f.close()
    if int(data[2])+diff <= 0:
        data[2] = 0
    elif int(data[2])+diff >= 100:
        data[2] = 100
    else:
        data[2] = int(data[2]) + diff
    f = open("info.txt", "w")
    f.write(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    f.close()

def get_info_arr():
    f = open("info.txt", "r")
    data = f.readline().replace('\n', '').split(' ')
    f.close()
    return data

if __name__ == "__main__":
    print(get_info_arr())
    f = open("info.txt", "r")
    data = f.readline().replace('\n', '').split(' ')
    f.close()
    data[0] = get_temperature.get_value()
    data[1] = get_moisture.get_value()
    if int(data[2]) - 10 <= 0:
        data[2] = 0
    else:
        data[2] = int(data[2]) - 10
    f = open("info.txt", "w")
    f.write(str(data[0])+" "+str(data[1])+" "+str(data[2]))
    f.close()
