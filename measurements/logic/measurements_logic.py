from ..models import Measurement
from variables.models import Variable

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(mea_pk):
    measurement = Measurement.objects.get(pk=mea_pk)
    return measurement

def update_measurement(mea_pk, new_mea):
    measurement = get_measurement(mea_pk)
    measurement.value = new_mea["value"]
    measurement.unit = new_mea["unit"]
    measurement.save()
    return measurement

def create_measurement(mea):
    var_obj = Variable.objects.get(pk=mea["variable"])
    measurement = Measurement(variable=var_obj, value=mea["value"], unit=mea["unit"])
    measurement.save()
    return measurement

def remove_measurement(mea_pk):
    measurement = get_measurement(mea_pk)
    measurement.delete()
    return measurement