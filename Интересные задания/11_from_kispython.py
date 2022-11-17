import struct


def uint16uint32uint8(s, pointer):
    size = struct.unpack('>H', s[pointer:pointer + 2])[0]
    add = struct.unpack('>I', s[pointer + 2:pointer + 6])[0]
    a = struct.unpack('>' + 'B' * size, s[add:add + 1 * size])
    return list(a)


def uint16uint16char(s, pointer):
    buf = ""
    size = struct.unpack('>H', s[pointer:pointer + 2])[0]
    add = struct.unpack('>H', s[pointer + 2:pointer + 4])[0]
    a = struct.unpack('>' + 'c' * size, s[add:add + 1 * size])
    for el in a:
        buf += str(el)[2:3]
    return buf


def uint16uint16_in_B_structure(s, pointer):
    result = []
    size = struct.unpack('>H', s[pointer:pointer + 2])[0]
    add = struct.unpack('>H', s[pointer + 2:pointer + 4])[0]
    for i in range(0, size):
        result.append({
            'B1': struct.unpack('>I', s[add:add + 4])[0],
            'B2': struct.unpack('>H', s[add + 4:add + 6])[0]
        })
        add += 6
    return result


def main(s):
    a7 = struct.unpack('>H', s[39:41])[0]
    c6 = struct.unpack('>I', s[a7+66:a7+70])[0]
    out_dict = {
        'A1': uint16uint16_in_B_structure(s, 5),
        'A2': struct.unpack('>d', s[9:17])[0],
        'A3': struct.unpack('>q', s[17:25])[0],
        'A4': uint16uint16char(s, 25),
        'A5': struct.unpack('>Q', s[29:37])[0],
        'A6': struct.unpack('>h', s[37:39])[0],
        'A7': {
            'C1': uint16uint32uint8(s, a7),
            'C2': struct.unpack('>Q', s[a7+6:a7+14])[0],
            'C3': struct.unpack('>I', s[a7 + 14:a7 + 18])[0],
            'C4': list(struct.unpack('>5Q', s[a7 + 18:a7 + 58])),
            'C5': struct.unpack('>Q', s[a7 + 58:a7 + 66])[0],
            'C6': {
                'D1': struct.unpack('>H', s[c6:c6+2])[0],
                'D2': struct.unpack('>I', s[c6+2:c6+6])[0]
            }
        },
        'A8': struct.unpack('>Q', s[41:49])[0]
    }
    return out_dict
