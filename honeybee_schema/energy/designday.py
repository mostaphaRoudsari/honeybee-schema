"""Simulation Parameter Schema"""
from pydantic import BaseModel, Field, constr
from typing import Union
from enum import Enum
from ..datetime import Date

from ._base import NamedEnergyBaseModel


class DryBulbCondition(BaseModel):
    """Used to specify dry bulb conditions on a design day."""

    type: constr(regex='^DryBulbCondition$') = 'DryBulbCondition'

    dry_bulb_max: float = Field(
        ...,
        ge=-90,
        le=70,
        description='The maximum dry bulb temperature on the design day [C].'
    )

    dry_bulb_range: float = Field(
        ...,
        ge=0,
        description='The difference between min and max temperatures on the' 
            'design day [C].'
    )


class HumidityTypes(str, Enum):
    wetbulb = 'Wetbulb'
    dewpoint = 'Dewpoint'
    humidity_ratio = 'HumidityRatio'
    enthalpy = 'Enthalpy'


class HumidityCondition(BaseModel):
    """Used to specify humidity conditions on a design day."""

    type: constr(regex='^HumidityCondition$') = 'HumidityCondition'

    humidity_type: HumidityTypes

    humidity_value: float = Field(
        ...,
        description='The value correcponding to the humidity_type.'
    )

    barometric_pressure: float = Field(
        101325,
        ge=31000,
        le=120000,
        description='Barometric air pressure on the design day [Pa].'
    )

    rain: bool = Field(
        default=False,
        description='Boolean to indicate rain on the design day.'
    )

    snow_on_ground: bool = Field(
        default=False,
        description='Boolean to indicate snow on the ground during the design day.'
    )


class WindCondition(BaseModel):
    """Used to specify wind conditions on a design day."""

    type: constr(regex='^WindCondition$') = 'WindCondition'

    wind_speed: float = Field(
        ...,
        ge=0,
        le=40,
        description='Wind speed on the design day [m/s].'
    )

    wind_direction: float = Field(
        0,
        ge=0,
        le=360,
        description='Wind direction on the design day [degrees].'
    )


class ASHRAEClearSky(BaseModel):
    """Used to specify sky conditions on a design day."""

    type: constr(regex='^ASHRAEClearSky$') = 'ASHRAEClearSky'

    date: Date = Field(
        ...,
        description='Date for the day of the year on which the design day occurs.'
    )

    clearness: float = Field(
        ...,
        ge=0,
        le=1.2,
        description='Value between 0 and 1.2 that will get multiplied by the '
            'irradinace to correct for factors like elevation above sea level.'
    )

    daylight_savings: bool = Field(
        default=False,
        description='Boolean to indicate whether daylight savings time is active '
            'on the design day.'
    )


class ASHRAETau(BaseModel):
    """Used to specify sky conditions on a design day."""

    type: constr(regex='^ASHRAETau$') = 'ASHRAETau'

    date: Date = Field(
        ...,
        description='Date for the day of the year on which the design day occurs.'
    )

    tau_b: float = Field(
        ...,
        ge=0,
        le=1.2,
        description='Value for the beam optical depth. Typically found in .stat files.'
    )

    tau_d: float = Field(
        ...,
        ge=0,
        le=3,
        description='Value for the diffuse optical depth. Typically found in .stat files.'
    )

    daylight_savings: bool = Field(
        default=False,
        description='Boolean to indicate whether daylight savings time is active '
            'on the design day.'
    )


class DesignDayTypes(str, Enum):
    summer_design_day = 'SummerDesignDay'
    winter_design_day = 'WinterDesignDay'
    sunday = 'Sunday'
    monday = 'Monday'
    tuesday = 'Tuesday'
    wednesday = 'Wednesday'
    thursday = 'Thursday'
    friday = 'Friday'
    holiday = 'Holiday'
    custom_day1 = 'CustomDay1'
    custom_day2 = 'CustomDay2'


class DesignDay(NamedEnergyBaseModel):
    """An object representing design day conditions."""

    type: constr(regex='^DesignDay$') = 'DesignDay'

    day_type: DesignDayTypes

    dry_bulb_condition: DryBulbCondition = Field(
        ...,
        description='A DryBulbCondition describing temperature conditions on '
            'the design day.'
    )

    humidity_condition: HumidityCondition = Field(
        ...,
        description='A HumidityCondition describing humidity and precipitation '
            'conditions on the design day.'
    )

    wind_condition: WindCondition = Field(
        ...,
        description='A WindCondition describing wind conditions on the design day.'
    )

    sky_condition: Union[ASHRAEClearSky, ASHRAETau] = Field(
        ...,
        description='A SkyCondition (either ASHRAEClearSky or ASHRAETau) describing '
            'solar irradiance conditions on the design day.'
    )


if __name__ == '__main__':
    print(DesignDay.schema_json(indent=2))