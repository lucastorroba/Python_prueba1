def binario_a_decimal(binario):
    try:
        int(binario, 2)
        return True
    except:
        return False


print(binario_a_decimal("fgdgr"))
