import json
import ctypes

C_MAX = 0xffffffff

# 定义数据类型
UCHAR       = ctypes.c_ubyte
USHORT      = ctypes.c_ushort
INT32       = ctypes.c_int32
UINT32      = ctypes.c_uint32
INT64       = ctypes.c_int64
UINT64      = ctypes.c_uint64
INT_ID      = ctypes.c_int64
INT_REG     = ctypes.c_uint32
INT_MEMADDR = ctypes.c_uint32

## 定义枚举
ENUM_FILTER_MODE_AND = ctypes.c_int32(1)
ENUM_FILTER_MODE_OR  = ctypes.c_int32(0)


## 定义数据结构
class RecordTrace(ctypes.Structure):
    _fields_ = [
        ('id',              INT_ID),
        ('eip',             INT_REG),
        ('eflags',          INT_REG),
        ('hex_code',        UCHAR*16),
        ('op_valuesbefore', UCHAR*16*3),
        ('op_valuesafter',  UCHAR*16*3),
        ('op_sizes',        UINT32*3),
        ('op_addrs',        INT_REG*3),
        ('regs',            INT_REG*8),
        ('fpstt',           UINT32),
        ('fpus',            USHORT),
        ('fpuc',            USHORT),
        ('fp_tags',         UCHAR*8),
        ('fs_base',         INT64),
        ('gs_base',         INT64),
        ('pid',             UINT32),
        ('tid',             UINT32),
    ]

    # 获取 dict 格式数据
    @property
    def dict(self):
        data = {
            "id"        : int(self.id),
            "eip"       : "0x%08x" % int(self.eip),
            "eflags"    : int(self.eflags),
            "hex_code"  : str(bytes(self.hex_code)),
            "op_0"      : str([bytes(_) for _ in self.op_valuesbefore]),
            "op_1"      : str([bytes(_) for _ in self.op_valuesafter]),
            "op_size"   : [int(_) for _ in self.op_sizes],
            "op_addr"   : ['0x%08x'%_ for _ in self.op_addrs],
            "regs"      : ['0x%08x'%_ for _ in self.regs],
        }
        return data

    @property
    def json(self):
        return json.dumps(self.dict, ensure_ascii="False")

class RecordFull(ctypes.Structure):
    _fields_ = [
        ('rid', ctypes.c_uint64),   # Row Number
        ('r', RecordTrace),         # RecordTrace 结构体
        ('_asm', ctypes.c_char*32)  # ASM 汇编字符串
    ]

    @property
    def dict(self):
        data = self.r.dict
        data.update({'rid': int(self.rid), 'asm': bytes(self._asm).decode('ASCII')})
        return data.copy()

    @property
    def json(self):
        return json.dumps(self.dict, ensure_ascii="False")

## 定义 PyTraceArray Python数据类型
class PyTraceArray(object):
    def __init__(self, trace: RecordFull, count: int) -> None:
        self._trace = trace
        self._count = int(count)

    def __bool__(self):
        return bool(self.count)

    def __add__(self, another: object):
        assert isinstance(another, PyTraceArray)
        if (self and another is False):
            return PyTraceArray.null()
        elif (not self):
            return another.copy()
        elif (not another):
            return self.copy()
        count = self.count + another.count
        nArray = (RecordFull * count)()
        for i in range(self.count):
            nArray[i] = self.trace[i]
        for i in range(another.count):
            nArray[self.count+i] = another.trace[i]
        return PyTraceArray(nArray, count)

    def __iter__(self):
        data = []
        for i in range(self.count):
            t = self.trace[i]
            data.append(t.dict)
        return iter(data)

    @property
    def json(self):
        return json.dumps(list(self), ensure_ascii=False)

    @classmethod
    def null(cls):
        ret = cls(None, 0)
        return ret

    @property
    def trace(self):
        return self._trace
    
    @property
    def count(self):
        return self._count

    def copy(self):
        nArray = (RecordFull*self.count)()
        for i in range(self.count):
            nArray[i] = self.trace[i]
        return PyTraceArray(nArray, self.count)

    def show(self):
        for i in range(self.count):
            t = self.trace[i]
            assert isinstance(t, RecordFull)
            print("rid: %08d, id: %08d, eip: 0x%08x, asm: %s" % (t.rid, t.r.id, t.r.eip, t._asm) )
