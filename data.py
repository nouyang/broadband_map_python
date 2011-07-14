#!/usr/bin/env python

doclinks = ['http://www.broadbandmap.gov/developer/api/almanac-api-parameters', 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-a-state', 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-the-nation', 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-a-state', 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-the-nation', 'http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-id', 'http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-name', 'http://www.broadbandmap.gov/developer/api/bip-funding-api-nation', 'http://www.broadbandmap.gov/developer/api/broadband-provider-api-all-providers', 'http://www.broadbandmap.gov/developer/api/broadband-provider-api-by-provider-name', 'http://www.broadbandmap.gov/developer/api/broadband-summary-api-by-geography-type-and-geography-id', 'http://www.broadbandmap.gov/developer/api/broadband-summary-api-nation', 'http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-id', 'http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-name', 'http://www.broadbandmap.gov/developer/api/btop-funding-api-nation', 'http://www.broadbandmap.gov/developer/api/census-api-by-coordinates', 'http://www.broadbandmap.gov/developer/api/census-api-by-fips-code', 'http://www.broadbandmap.gov/developer/api/census-api-by-geography-name', 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-closest-by-latitude-and-longitude', 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-id', 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-name', 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-nation', 'http://www.broadbandmap.gov/developer/api/demographics-api-by-coordinates', 'http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-id', 'http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-name', 'http://www.broadbandmap.gov/developer/api/demographics-api-nation', 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-id', 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type', 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-and-geography-name', 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-within-a-state', 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-name-of-specific-geography-type-within-a-state', 'http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-id', 'http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-name', 'http://www.broadbandmap.gov/developer/api/speed-test-api-minimum-and-maximum-quartile-speeds-by-geography-type', 'http://www.broadbandmap.gov/developer/api/speed-test-api-nation', 'http://www.broadbandmap.gov/developer/api/wireless-broadband-api', 'http://www.broadbandmap.gov/developer/api/wireline-broadband-api']

# Structure:
# key: documentation URL
# item: list, 1. documentation text 2. API call format 3. Sample API call 4..n. Parameters and parameter descriptions
docdata = {'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-id': [u'This API allows you to find a geography of a specified geography type by the geography id.', u'http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}/id/{geographyId}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/geography/congdistrict/id/0111101?format=json', u'geographyType : specify either one of the following geography type: county, censusplace, msa, usf,  statesenate, statehouse, congdistrict, tribalnation', u'geographyId: specify the geography id to search for demographics.', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-the-nation': [u'This API is designed to find the rankings by any geography type within the nation with a specific census metric (population or household) and ranking metric (any of the metrics from provider, demographic, technology or speed). Support for full list of rankings by nation is not allowed for geography types (e.g., county, census place, usf) so only the top ten and bottom ten rankings would be returned through the API.', u'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/nation/{censusMetric}/{rankingMetric}/{geographyType}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}', u'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/nation/population/wirelineproviderequals0/county?format=json&order=asc', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u"censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'", u'rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done', u'geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict, tribalnation', u"sortOrder - specify 'asc' for ascending order(default) and 'desc' for descending order", u'properties - specify the properties comma delimited to be included in the result', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-name-of-specific-geography-type-within-a-state': [u'This API returns geographies by name of a specific geography type within a state.', u'http://www.broadbandmap.gov/broadbandmap/geography/state/{stateFips}/{geographyType}/name/{geographyName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/geography/state/17/county/name/mar?format=json', u'stateFips: specify the state fips to search for the specific geography types.', u'geographyType : specify either one of the following geography type: county, censusplace, msa, usf,  statesenate, statehouse, congdistrict, tribalnation', u'geographyName: specify the geography name with atleast 3 leading characters.', u'maxResults: specify the maximum results to be returned. defaulted to 100.', u'all: if true returns the complete set of results.', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/broadband-summary-api-nation': [u'This API returns broadband summary data for the entire United States. It is designed to retrieve broadband summary data and census metrics (population or households) combined as search criteria. The data includes wireline and wireless providers, different technologies and broadband speeds reported in the particular area being searched for on a scale of 0 to 1.', u'http://www.broadbandmap.gov/broadbandmap/analyze/{dataVersion}/summary/{censusMetricType}/nation?format={format}&callback={callback}', u'http://www.broadbandmap.gov/broadbandmap/analyze/fall2010/summary/population/nation?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u"censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'", u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/broadband-provider-api-all-providers': [u'The Broadband Provider API searches for all providers with a specified name.', u'http://www.broadbandmap.gov/broadbandmap/provider?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/provider?format=json', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-id': [u'This API allows the user to retrieve the broadband availability among the Community Anchor Institutions by geography type and ID.', u'http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/{geographyType}/ids/{geographyIds}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/cai/fall2010/state/ids/01,02?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/wireless-broadband-api': [u'This API returns all the wireless providers within a US census block given a passed latitude and longitude.', u'http://www.broadbandmap.gov/broadbandmap/broadband/{dataVersion}/wireless?latitude={latitude}&longitude=-{longitude}&maxresults={maxResults}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/broadband/fall2010/wireless?latitude=42.456&longitude=-74.987&format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'latitude - latitude of a point. Example: 41.486857', u'longitude - longitude of a point. Example: -71.294392', u'maxResults - specify the maximum results to be returned - defaulted to 100', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-nation': [u'This API allows the user to retrieve the broadband availability among the Community Anchor Institutions for the entire United States.', u'http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/nation?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/cai/fall2010/nation?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'format (optional) - Valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-name': [u'This API returns the speed test results for a particular geography type (e.g., state, congressional district) and geography name (e.g., Virginia).', u'http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/names/{geographyNames}?testtype={speedTestType}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/speedtest/state/names/alabama,arizona?format=json', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed', u'speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-and-geography-name': [u'This API returns geographies by name of a specific geography type.', u'http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}/name/{geographyName}?maxresults={maxResults}&all={all}&{format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/geography/censusplace/name/sei?format=json', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyName - specify the geography name with at least 3 leading characters', u'maxResults - specify the maximum results to be returned - defaulted to 100', u'all - if true returns the complete set of results', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-name': [u'This API allows the user to search for the demographic information for a particular geography type and geography name.', u'http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/{geographyType}/names/{geographyNames}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/county/names/jersey,jefferson?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/demographics-api-nation': [u'This API allows the user to search for the demographic information for the whole nation.', u'http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/nation?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/nation?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'format (optional) - Valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-name': [u'This API returns BTOP funding information by state name.', u'http://www.broadbandmap.gov/broadbandmap/btop/states/{stateNames}?format={format}', u'http://www.broadbandmap.gov/broadbandmap/btop/states/alaska,alabama?format=json', u'stateNames - specify the state names to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-id': [u'This API allows the user to find the BIP funding allocated to states by specifying the state fips code. ', u'http://www.broadbandmap.gov/broadbandmap/bip/stateids/{stateIds}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/bip/stateids/01,02?format=json', u'stateIds: specify the state fips codes to search for separated by commas and a maximum of 10 are allowed', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/speed-test-api-nation': [u'This API returns all the speed test results for the entire United States.', u'http://www.broadbandmap.gov/broadbandmap/speedtest/nation?testtype={speedTestType}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/speedtest/nation?format=json', u'speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/demographics-api-by-geography-type-and-geography-id': [u'This API allows the user to search for the demographic information for a particular geography type and geography ID', u'http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/{geographyType}/ids/{geographyIds}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/county/ids/17081,17083?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/speed-test-api-minimum-and-maximum-quartile-speeds-by-geography-type': [u'This API returns the minimum and maximum quartile speeds by geography type within the nation.', u'http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/quartile?testtype={speedTestType}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/speedtest/state/quartile?format=json', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-type-within-a-state': [u'This API is designed to find the rankings by any geography type within the state with a specific census metric (population or household) and ranking metric (any of the metrics from provider, demographic, technology or speed). Only the top ten and bottom ten rankings would be returned through the API if the result set is greater than 500; otherwise full ranking list be returned.', u'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}', u'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county?format=json&order=asc', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'stateId - specify the state fips code within which the ranking should be done', u"censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'", u'rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done', u'geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict', u"sortOrder - specify 'asc' for ascending order(default) and 'desc' for descending order", u'properties - specify the properties comma delimited to be included in the result', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/almanac-api-parameters': [u'The Almanac API is designed to get all almanac parameters used by the Almanac API for ranking.', u'http://www.broadbandmap.gov/broadbandmap/almanac/parameters?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/almanac/parameters?format=json', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/wireline-broadband-api': [u'This API returns all the wireline providers within a US census block given a passed latitude and longitude.', u'http://www.broadbandmap.gov/broadbandmap/broadband/{dataVersion}/wireline?latitude={latitude}&longitude=-{longitude}&maxresults={maxResults}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/broadband/fall2010/wireline?latitude=42.456&longitude=-74.987&format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'latitude - latitude of a point. Example: 41.486857', u'longitude - longitude of a point. Example: -71.294392', u'maxResults - specify the maximum results to be returned - defaulted to 100', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-the-nation': [u'This API is designed to find the rankings by any geography ID within the nation with a specific census metric (population or household) and ranking metric (any of the metrics from provider, demographic, technology or speed). The results are the top ten and bottom ten rankings within the nation for the particular geography type and my area rankings include +/- 5 rankings from the my area rank.', u'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/nation/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}', u'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/nation/population/wirelineproviderequals0/county/id/51117?format=json&order=asc', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u"censusMetricType - specify the census metric by which the data has to be aggregated. It can be either 'population' or 'household'", u'rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done', u'geographyType - specify either one of the following geography type: state, censusplace, msa, usf, county, statesenate, statehouse, congdistrict, tribalnation', u'geographyId - specify the my area geography ID to be ranked', u"sortOrder - specify 'asc' for ascending order (default) and 'desc' for descending order", u'Properties - specify the properties comma delimited to be included in the results'], 'http://www.broadbandmap.gov/developer/api/bip-funding-api-by-state-name': [u'This API allows the user to find the BIP funding allocated to states by specifying the state names.', u'http://www.broadbandmap.gov/broadbandmap/bip/states/{stateNames}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/bip/states/alaska,alabama?format=json', u'stateNames: specify the state names to search for separated by commas and a maximum of 10 are allowed', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/btop-funding-api-nation': [u'This API returns BTOP funding for the entire United States.', u'http://www.broadbandmap.gov/broadbandmap/btop/nation?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/btop/nation?format=json', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-closest-by-latitude-and-longitude': [u'This API returns the closest community anchor institutions by latitude and longitude', u'http://www.broadbandmap.gov/broadbandmap/cai/closest?latitude={latitude}&longitude={longitude}&maxresults={maxResults}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/cai/closest?latitude=41.486857&longitude=-71.294392&maxresults=2&format=json', u'latitude - latitude of a point. Example: 41.486857', u'longitude - longitude of a point. Example: -71.294392', u'Maxresults (optional) - maximum number of results (default 25, maximum 100)', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/btop-funding-api-by-state-id': [u'This API returns BTOP funding information by state ID.', u'http://www.broadbandmap.gov/broadbandmap/btop/stateids/{stateIds}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/btop/stateids/01,02?format=json', u'stateIds - specify the state fips codes to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/speed-test-api-by-geography-type-and-geography-id': [u'This API returns the speed test results for a particular geography type (e.g., state, congressional district) and geography ID.', u'http://www.broadbandmap.gov/broadbandmap/speedtest/{geographyType}/ids/{geographyIds}?testtype={speedTestType}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/speedtest/state/ids/01,02?format=json', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed', u'speedTestType (optional) - specify the speed test type among any,ookla,mlab with default being any', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/census-api-by-coordinates': [u'This API returns the US Census Block geography ID information given a passed Latitude and Longitude.', u'http://www.broadbandmap.gov/broadbandmap/census/{geographyType}?latitude={latitude}&longitude={longitude}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/census/block?latitude=42.456&longitude=-74.987&format=json', u'geographyType - specify one of the following geography type: state, county, tract, block, congdistrict, statehouse, statesenate, censusplace, msa, all (to retrieve all the geographies)', u'latitude - latitude of a point. Example: 41.486857', u'longitude - longitude of a point. Example: -71.294392', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/census-api-by-fips-code': [u'This API finds the geography of a specified geography type by geography id within the entire United States.', u'http://www.broadbandmap.gov/broadbandmap/census/{geographyType}/fips/{geographyId}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/census/state/fips/36?format=json', u'geographyType - specify one of the following geography types: state, county, tract, block, congdistrict, statehouse, statesenate, censusplace, msa, tribal, usf', u'fipsCode - FIPS code (unique identifier)', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type': [u'This API allows users to find all geographies of a specified geography type.', u'http://www.broadbandmap.gov/broadbandmap/geography/{geographyType}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/geography/congdistrict?format=json&maxresults=1000', u'geographyType: specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'maxResults: specify the maximum results to be returned. defaulted to 100', u'all: if true returns the complete set of results', u'format (optional): Valid formats are xml, json, jsonp with default being xml', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/broadband-provider-api-by-provider-name': [u'The Broadband Provider API searches for all providers with a specified name.', u'http://www.broadbandmap.gov/broadbandmap/provider/name/{providerName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/provider/name/alb?format=json', u'providerName: specify the provider name with atleast 3 leading characters.', u'all: if true returns the complete set of results.', u'maxResults: specify the maximum results to be returned. defaulted to 20.', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/almanac-api-ranking-by-geography-id-within-a-state': [u"This API is designed to find the rankings by geography within the state for a specific metric (population or household) and rank (any of the metrics from provider, demographic, technology or speed). The results are the top ten and bottom ten records within the state for the particular geography type and my area rankings. Additionally we include +/- 5 rankings from the 'my' area rank.", u'http://www.broadbandmap.gov/broadbandmap/almanac/{dataVersion}/rankby/state/{stateId}/{censusMetric}/{rankingMetric}/{geographyType}/id/{geographyId}?properties={properties}&format={format}&callback={functionName}&order={sortOrder}&properties={properties}', u'http://www.broadbandmap.gov/broadbandmap/almanac/fall2010/rankby/state/01/population/wirelineproviderequals0/county/id/01101?format=json&order=asc', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010', u'stateId - specify the state fips code within which the ranking should be done', u'censusMetricType - specify the census metric by which the data has to be aggregated. It can be either population or household', u'rankingMetric - specify one of the various metrics from demographics, technologies, speeds or providers by which the ranking will be done', u'geographyType - specify one of the following geography type: censusplace, msa, usf, county, statesenate, statehouse, congdistrict', u'geographyId - specify the my area geography ID to be ranked', u"sortOrder - specify 'asc' for ascending order (default) and 'desc' for descending order", u'properties - specify the properties comma delimited to be included in the result', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/community-anchor-institutions-api-by-geography-type-and-geography-name': [u'This API allows the user to retrieve the broadband availability among the Community Anchor Institutions by geography name and type.', u'http://www.broadbandmap.gov/broadbandmap/cai/{dataVersion}/{geographyType}/names/{geographyNames}?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/cai/fall2010/state/names/alabama,arizona?format=json', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010.', u'geographyType - specify either one of the following geography type: state, county, censusplace, msa, usf, statesenate, statehouse, congdistrict, tribalnation', u'geographyNames - specify the geography names to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/bip-funding-api-nation': [u'This API allows the user to retrieve the BIP funding allocation for the whole nation. ', u'http://www.broadbandmap.gov/broadbandmap/bip/nation?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/bip/nation?format=json', u'stateIds: specify the state fips codes to search for separated by commas and a maximum of 10 are allowed', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.'], 'http://www.broadbandmap.gov/developer/api/geography-lookup-api-by-geography-type-within-a-state': [u'This API returns all geographies of specific geography type within a state.', u'http://www.broadbandmap.gov/broadbandmap/geography/state/{stateFips}/{geographyType}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/geography/state/01/msa?format=json', u'stateFips - specify the state fips to search for the specific geography types', u'geographyType - specify either one of the following geography type: county, censusplace, msa, usf,  statesenate, statehouse, congdistrict, tribalnation', u'maxResults - specify the maximum results to be returned - defaulted to 100', u'all - if true returns the complete set of results', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/broadband-summary-api-by-geography-type-and-geography-id': [u'This API returns broadband summary data by geography IDs for a specific geography type. It is designed to retrieve broadband summary data by geography and census metrics (population or households) combined as search criteria. The data includes wireline and wireless providers, different technologies and broadband speeds reported in the particular area being searched for on a scale of 0 to 1.', u'http://www.broadbandmap.gov/broadbandmap/analyze/{dataVersion}/summary/{censusMetricType}/{geographyType}/ids/{geographyIds}?format={format}&callback={callback}', u'http://www.broadbandmap.gov/broadbandmap/analyze/fall2010/summary/population/state/ids/10?format=json ', u'dataVersion - specify the data version for search(no defaults). Examples: fall2010.', u'censusMetricType - specify the census metric by which the data has to be aggregated. It can be either population or household', u'geographyType - specify either one of the following geography type: state, censusplace, msa, county, statesenate, statehouse, congdistrict, usf, tribalnation', u'geographyIds - specify the geography IDs to search for separated by commas and a maximum of 10 are allowed', u'format (optional) - valid formats are xml, json, jsonp with default being xml', u'callback (optional) - jsonp callback function name'], 'http://www.broadbandmap.gov/developer/api/census-api-by-geography-name': [u'This API finds all the geographies specified by a geography name (e.g., Washington) of a specific geography type (e.g., congressional district) within the entire United States.', u'http://www.broadbandmap.gov/broadbandmap/census/{geographyType}/{geographyName}?maxresults={maxResults}&all={all}&format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/census/county/fai?format=json', u'geographyType - specify one of the following geography types: state, county, tract, block, congdistrict, statehouse, statesenate, censusplace, msa', u'geographyName - specify the geography name with at least 3 leading characters', u'maxResults - specify the maximum results to be returned - defaults to 100', u'all - if true returns the complete set of results.', u'format (optional) - valid formats are xml, json, jsonp with default being xml'], 'http://www.broadbandmap.gov/developer/api/demographics-api-by-coordinates': [u'find the demographics data from the coordinates.', u'http://www.broadbandmap.gov/broadbandmap/demographic/{dataVersion}/coordinates?format={format}&callback={functionName}', u'http://www.broadbandmap.gov/broadbandmap/demographic/fall2010/coordinates?latitude=42.456&longitude=-74.987&format=json', u'dataVersion : specify the data version for search(no defaults). Examples: fall2010', u'latitude: latitude of a point.', u'longitude: longitude of a point.', u'format (optional): Valid formats are xml, json, jsonp with default being xml.', u'callback (optional): jsonp callback function name.']}
