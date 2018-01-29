#!/usr/bin/python
# -*- coding: utf-8 -*-
import testlink

# manual = 1  # 手动
# automation = 2  # 自动

# 连接test link
# url = "http://10.235.102.234/testlink1.9.3/lib/api/xmlrpc.php"
# key = "46fb9c9eb7268da9e2dbbda1492b9575"
# tlc = testlink.TestlinkAPIClient(url, key)


class TL(object):
	#8.发送测试结果给testlink
	def report_test_result(self,test_plan_id, test_case_id, test_result, build_id, url, key):
		u'''usage:
		Report Test Result    ${test_plan_id}    ${test_case_id}    ${result}    ${buildid}    ${url}    ${key} 
		'''
		tlc = testlink.TestlinkAPIClient(url, key)
		tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                       testcaseexternalid=test_case_id, platformname="windows7", buildid=build_id)
	def decode(self,name):
		return customerstr.decode('utf-8')

'''		
tlc.listProjects()
Name: cyclos ID: 1
Name: miwifi ID: 12

tlc.getProjectTestPlans(12)

tlc.getProjectTestPlans(test_project_id)
[{'active': '1',
  'id': '203',
  'is_public': '1',
  'name': 'dailytest',
  'notes': '',
  'testproject_id': '12'},
 {'active': '1',
  'id': '13',
  'is_public': '1',
  'name': 'r2d_ota',
  'notes': '',
  'testproject_id': '12'}]
  
tlc.getTestCasesForTestPlan(13) 		
		
		
test_case_name = "loginPageCheck"
test_case_id = 'mi-2'
test_project_id = 12
test_plan_id = 13
test_result = 'p'   # 'p' or 'f'
platformname = "windows7"

  
  
tlc.getTestCaseIDByName(test_case_name)		
tlc.getLastExecutionResult(test_plan_id, test_case_id)  
tlc.getTestCase()
tlc.getTestCasesForTestPlan(13)
tlc.getTestCasesForTestSuite()


report_test_result(test_plan_id, test_case_id, test_result)

tlc.reportTCResult(None, 13, None, 'p', "", guess=True,testcaseexternalid='mi-2',platformname="windows7")

tlc.reportTCResult(None, 203, None, 'f', "", guess=True,testcaseexternalid='mi-4',platformname="windows7",buildid=10)

buildid = 'exec_on_build': '4',		
		
'''		
		
		
		
		
# Class TestLinkp(object):
	# #8.发送测试结果给testlink
	# def report_test_result(test_plan_id, test_case_id, test_result):
		# tlc.reportTCResult(None, test_plan_id, None, test_result, "", guess=True,
                       # testcaseexternalid=test_case_id, platformname="windows7")

					   
#3.获取testlink上的信息：

# def get_information_test_project():
    # print("Number of Projects      in TestLink: %s " % tlc.countProjects())
    # print("Number of Platforms  (in TestPlans): %s " % tlc.countPlatforms())
    # print("Number of Builds                   : %s " % tlc.countBuilds())
    # print("Number of TestPlans                : %s " % tlc.countTestPlans())
    # print("Number of TestSuites               : %s " % tlc.countTestSuites())
    # print("Number of TestCases (in TestSuites): %s " % tlc.countTestCasesTS())
    # print("Number of TestCases (in TestPlans) : %s " % tlc.countTestCasesTP())
    # tlc.listProjects()

# #4.获取 test suite

# def get_test_suite():
    # projects = tlc.getProjects()
    # top_suites = tlc.getFirstLevelTestSuitesForTestProject(projects[0]["id"])
    # for suite in top_suites:
        # print suite["id"], suite["name"]


# #5.创建测试用例集

# def create_test_suite(project_id, test_suite_name, test_suite_describe, father_id):
    # if father_id == "":
        # tlc.createTestSuite(project_id, test_suite_name, test_suite_describe)
    # else:
        # tlc.createTestSuite(project_id, test_suite_name, test_suite_describe, parentid=father_id)

# #6.创建测试用例

# def create_test_case(father_id, data):
    # tlc.initStep(data[0][2], data[0][3], automation)
    # for i in range(1, len(data)):
        # tlc.appendStep(data[i][2], data[i][3], automation)
    # tlc.createTestCase(data[0][0], father_id, "1", "timen.xu", "", preconditions=data[0][1])

# #7.获取测试用例
# def get_test_case(test_case_id):
    # test_case = tlc.getTestCase(None, testcaseexternalid=test_case_id)
    # for i in test_case:
        # print "序列", "执行步骤", "预期结果"
        # for m in i.get("steps"):
            # print m.get("step_number"), m.get("actions"), m.get("expected_results")

			   
'''

In [31]: get_information_test_project()
Number of Projects      in TestLink: 2
Number of Platforms  (in TestPlans): 3
Number of Builds                   : 2
Number of TestPlans                : 4
Number of TestSuites               : 3
Number of TestCases (in TestSuites): 281
Number of TestCases (in TestPlans) : 23



  tlc.getTestCaseIDByName(test_case_name)		
  [{'id': '15',
  'name': 'loginPageCheck',
  'parent_id': '14',
  'tc_external_id': '1',
  'tsuite_name': 'login'}]		
  
    
  tlc.getTestCasesForTestPlan(13)
  '59': {'2': {'active': '1',
  'assigned_build_id': '4',
  'assigner_id': '1',
  'exec_id': '510',
  'exec_on_build': '4',
  'exec_on_tplan': '13',
  'exec_status': 'p',
  'executed': '60',
  'execution_notes': 'memo',
  'execution_order': '160',
  'execution_run_type': '2',
  'execution_ts': '2016-12-06 03:48:51',
  'execution_type': '1',
  'external_id': '20',
  'feature_id': '43',
  'importance': '2',
  'linked_by': '1',
  'linked_ts': '2015-11-06 10:57:36',
  'name': 'testcase20',
  'platform_id': '2',
  'platform_name': 'windows7',
  'priority': '4',
  'status': '1',
  'summary': '',
  'tc_id': '59',
  'tcversion_id': '60',
  'tcversion_number': '1',
  'tester_id': '1',
  'testsuite_id': '21',
  'tsuite_name': 'homepage',
  'type': '1',
  'urgency': '2',
  'user_id': '1',
  'version': '1',
  'z': '15'}}}
  
  
  
  
  
  '''
