import boto3
### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_lambda_functions(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # Lambda 클라이언트 생성
    lambda_client = session.client('lambda')
    
    # Lambda 함수 목록 가져오기
    response = lambda_client.list_functions()
    
    print("START")
    # 이름에 키워드가 포함된 함수 찾기
    for function in response.get('Functions', []):
        function_name = function['FunctionName']
        if keyword in function_name.lower():  # 소문자로 변환하여 비교
            print(f"\n\n\nFound Lambda Function: {function_name}")
            confirmation = input(f"\n\n\nDo you want to delete Lambda Function '{function_name}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\n\nDeleting Lambda Function: {function_name}")
                lambda_client.delete_function(FunctionName=function_name)
    print("\n\n\nEND")

if __name__ == '__main__':
    delete_lambda_functions(keyword)
