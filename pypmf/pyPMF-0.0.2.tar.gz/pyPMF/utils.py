import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def add_season(df, month=True, month_to_season=None):
    """
    Add a season column to the DataFrame df.

    parameters
    ----------

    df: Pandas DataFrame.
        The DataFrame to work with.
    month : add month number, default True

    return
    ------

    dfnew: a new pandas DataFrame with a 'season' columns.

    """

    if month_to_season is None:
        month_to_season = {1:'Winter', 2:'Winter', 3:'Spring', 4:'Spring', 5:'Spring', 6:'Summer',
                           7:'Summer', 8:'Summer', 9:'Fall', 10:'Fall', 11:'Fall',
                           12:'Winter'}

    dfnew = df.copy()

    # ensure we have date in index
    if "Date" in dfnew.index.names:
        dfnew["Date"] = dfnew.index.get_level_values("Date")
        dropDate = True
    elif 'Date' in dfnew.columns:
        dfnew["Date"] = pd.to_datetime(dfnew["Date"])
        dropDate = False
    else:
        print("No date given")
        return

    # add a new column with the number of the month (Jan=1, etc)
    dfnew["month"] = dfnew["Date"].apply(lambda x: x.month)
    # sort it. This is not mandatory.
    dfnew.sort_values(by="month", inplace=True)

    # add the season based on the month number
    dfnew["season"] = dfnew["month"].replace(month_to_season)

    if not month:
        dfnew.drop(columns=["month"], inplace=True)
    if dropDate:
        dfnew.drop(columns=["Date"], inplace=True)

    # and return the new dataframe
    return dfnew

def get_sourcesCategories(profiles):
    """Get the sources category according to the sources name.

    Ex. Aged sea salt → Aged_sea_salt

    :profiles: list
    :returns: list

    """
    possible_sources = {
        "Vehicular": "Traffic",
        "VEH": "Traffic",
        "VEH ind": "Traffic_ind",
        "Traffic_exhaust": "Traffic_exhaust",
        "Traffic_non-exhaust": "Traffic_non-exhaust",
        "VEH dir": "Traffic_dir",
        "Oil/Vehicular": "Traffic",
        "Oil": "Oil",
        "Vanadium rich": "Vanadium rich",
        "Road traffic/oil combustion": "Traffic",
        "Traffic": "Road traffic",
        "Traffic 1": "Traffic 1",
        "Traffic 2": "Traffic 2",
        "Primary traffic": "Road traffic",
        "Road traffic": "Road traffic",
        "Road trafic": "Road traffic",
        "Road traffic/dust": "Traffic/dust (Mix)",
        "Bio. burning": "Biomass_burning",
        "Bio burning": "Biomass_burning",
        "Comb fossile/biomasse": "Biomass_burning",
        "BB": "Biomass_burning",
        "Biomass_burning": "Biomass_burning",
        "Biomass Burning": "Biomass_burning",
        "Biomass burning": "Biomass_burning",
        "BB1": "Biomass_burning1",
        "BB2": "Biomass_burning2",
        "Sulfate-rich": "Sulfate_rich",
        "Sulphate-rich": "Sulfate_rich",
        "Nitrate-rich": "Nitrate_rich",
        "Sulfate rich": "Sulfate_rich",
        "Sulfate_rich": "Sulfate_rich",
        "Nitrate rich": "Nitrate_rich",
        "Nitrate_rich": "Nitrate_rich",
        "Secondary inorganics": "Secondary_inorganics",
        "Secondaire": "MSA_rich",
        "Secondary bio": "MSA_rich",
        "Secondary biogenic": "MSA_rich",
        "Secondary organic": "MSA_rich",
        "Secondary oxidation": "Secondary_oxidation",
        "Secondary biogenic oxidation": "Secondary_biogenic_oxidation",
        "Secondaire organique": "MSA_rich",
        # "Marine SOA": "Marine SOA",
        "Marine SOA": "MSA_rich",
        "MSA_rich": "MSA_rich",
        "MSA-rich": "MSA-rich",
        "MSA rich": "MSA_rich",
        "Secondary biogenic/sulfate": "SOA/sulfate (Mix)",
        "Marine SOA/SO4": "SOA/sulfate (Mix)",
        "Marine/HFO": "Marine/HFO",
        "Marine biogenic/HFO": "Marine/HFO",
        "Secondary biogenic/HFO": "Marine/HFO",
        "Marine bio/HFO": "Marine/HFO",
        "Marin bio/HFO": "Marine/HFO",
        "Sulfate rich/HFO": "Marine/HFO",
        "Marine secondary": "MSA_rich",
        "Marin secondaire": "MSA_rich",
        "HFO": "HFO",
        "HFO (stainless)": "HFO",
        "Marin": "MSA_rich",
        "Sea/road salt": "Sea-road salt",
        "Sea-road salt": "Sea-road salt",
        "sea-road salt": "Sea-road salt",
        "Road salt": "Salt",
        "Sea salt": "Salt",
        "Seasalt": "Salt",
        "Salt": "Salt",
        "Fresh seasalt": "Salt",
        "Sels de mer": "Salt",
        "Aged_salt": "Aged_salt",
        "Aged sea salt": "Aged_salt",
        "Aged seasalt": "Aged_salt",
        "Aged seasalt": "Aged_salt",
        "Aged salt": "Aged_salt",
        "Primary_biogenic": "Primary_biogenic",
        "Primary bio": "Primary_biogenic",
        "Primary biogenic": "Primary_biogenic",
        "Biogénique primaire": "Primary_biogenic",
        "Biogenique": "Primary_biogenic",
        "Biogenic": "Primary_biogenic",
        "Mineral dust": "Dust",
        "Mineral dust ": "Dust",
        "Resuspended_dust": "Resuspended_dust",
        "Resuspended dust": "Resuspended_dust",
        "Dust": "Dust",
        "Crustal dust": "Dust",
        "Dust (mineral)": "Dust",
        "Dust/biogénique marin": "Dust",
        "AOS/dust": "Dust",
        "Industrial": "Industrial",
        "Industry": "Industrial",
        "Industrie": "Industrial",
        "Industries": "Industrial",
        "Industry/vehicular": "Industry/traffic",
        "Industry/traffic": "Industry/traffic",
        "Industries/trafic": "Industry/traffic",
        "Cadmium rich": "Cadmium rich",
        "Fioul lourd": "HFO",
        "Arcellor": "Industrial",
        "Siderurgie": "Industrial",
        "Débris végétaux": "Plant_debris",
        "Chlorure": "Chloride",
        "PM other": "Other",
        "Undetermined": "Undertermined"
        }
    s = [possible_sources[k] for k in profiles]
    return s


def format_xaxis_timeseries(ax):
    """Format the x-axis timeseries with minortick = month and majortick=year

    :ax: the ax to format

    """
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
    ax.xaxis.set_minor_locator(mdates.MonthLocator())
    ax.xaxis.set_minor_formatter(mdates.DateFormatter("%b"))
    ax.set_xlabel("")

    plt.setp(ax.xaxis.get_majorticklabels(), rotation=00, ha="center")
