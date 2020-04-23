import json
full_dictionary = {"data": {
"region": {
"name": "Africa",
"avgAge": 19.7, "avgDailyIncomeInUSD": 5, "avgDailyIncomePopulation": 0.71
    },
  "periodType": "days",
  "timeToElapse": 58,
  "reportedCases": 674,
  "population": 66622705,
  "totalHospitalBeds": 1380614
}}
def covid19ImpactEstimator(dictionary):
    first_extract = dict([dictionary[key] for key in dictionary.keys()][0])
    second_extract = [s_val for value in first_extract.values() if type(value) is dict for s_val in value.values()]
    third_extract = [value for value in first_extract.values() if type(value) is not dict]
    full_extract = second_extract + third_extract
    class impact():
        """ To compute for the impact """
        reportedCases = full_extract[6]
        periodType = full_extract[4]
        timeToElapse = full_extract[5]
        totalHospitalBeds = full_extract[8]
        avgDailyIncomeInUSD = full_extract[2]
        avgDailyIncomePopulation = full_extract[3]

        def __init__(self):
            self.currentlyInfected = self.reportedCases * 10
            if self.periodType == 'days':
                self.infectionsByRequestedTime = self.currentlyInfected * (2 **(self.timeToElapse//3))
            elif self.periodType == 'weeks':
                self.infectionByRequestTime = self.currentlyInfected * ( 2 ** ((self.timeToElapse * 7)//3))
            elif self.periodType == 'months':
                self.infectionsByRequestedTime = self.currentlyInfected * (2 ** ((self.timeToElapse * 30)//3))
            self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
            self.hospitalBedsByRequestedTime = int((0.35 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)
            self.casesForICUByRequestedTime = 0.05 * self.infectionsByRequestedTime
            self.casesForVentilatorsByRequestedTime = 0.02 * self.infectionsByRequestedTime
            self.dollarsInFlight = self.infectionsByRequestedTime * self.avgDailyIncomePopulation * self.avgDailyIncomeInUSD * self.timeToElapse
            self.dictionary = {"currentlyInfected": self.currentlyInfected, "infectionsByRequestedTime": self.infectionsByRequestedTime, "severeCasesByRequestedTime": self.severeCasesByRequestedTime, "hospitalBedsByRequestedTime": self.hospitalBedsByRequestedTime, "casesForICUByRequestedTime": self.casesForICUByRequestedTime, "casesForVentilatorsByRequestedTime": self.casesForVentilatorsByRequestedTime, "dollarsInFlight": self.dollarsInFlight}
            self.j_dict = json.dumps(self.dictionary, indent = 2)

        def __str__(self):
            return "{}".format(self.j_dict)

    class severeImpact(impact):
        """ To compute for severe impact parallel to the impact class """
        def __init__(self):
            self.currentlyInfected = self.reportedCases * 50
            if self.periodType == 'days':
                self.infectionsByRequestedTime = self.currentlyInfected * (2 **(self.timeToElapse//3))
            elif self.periodType == 'weeks':
                self.infectionByRequestTime = self.currentlyInfected * ( 2 ** ((self.timeToElapse * 7)//3))
            elif self.periodType == 'months':
                self.infectionsByRequestedTime = self.currentlyInfected * (2 ** ((self.timeToElapse * 30)//3))
            self.severeCasesByRequestedTime = 0.15 * self.infectionsByRequestedTime
            self.hospitalBedsByRequestedTime = int((0.35 * 0.95 * self.totalHospitalBeds) - self.severeCasesByRequestedTime)
            self.casesForICUByRequestedTime = 0.05 * self.infectionsByRequestedTime
            self.casesForVentilatorsByRequestedTime = 0.02 * self.infectionsByRequestedTime
            self.dollarsInFlight = self.infectionsByRequestedTime * self.avgDailyIncomePopulation * self.avgDailyIncomeInUSD * self.timeToElapse
            self.dictionary = {"currentlyInfected": self.currentlyInfected, "infectionsByRequestedTime": self.infectionsByRequestedTime, "severeCasesByRequestedTime": self.severeCasesByRequestedTime, "hospitalBedsByRequestedTime": self.hospitalBedsByRequestedTime, "casesForICUByRequestedTime": self.casesForICUByRequestedTime, "casesForVentilatorsByRequestedTime": self.casesForVentilatorsByRequestedTime, "dollarsInFlight": self.dollarsInFlight}
            self.j_dict = json.dumps(self.dictionary, indent = 2)

        def __str__(self):
            return "{}".format(self.j_dict)
    # For proper output
    data = json.dumps(full_dictionary, indent = 2)
    test_case = impact()
    test_case_one = severeImpact()
    a = '{'
    b = '}'
    return '''{},
    "estimate":{}
    "impact": {} ,
    "severeImpact: {}
{}
    '''.format(data,a,test_case,test_case_one,b)


print(covid19ImpactEstimator(full_dictionary))
