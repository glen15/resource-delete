import boto3

### 지워야하는 리소스 키워드###
keyword = "TARGET KEYWORD"

### 대상 리전 지정 ###
region_name='TARGET REGION'

def delete_dynamodb_tables(keyword):
    # 서울 리전 세션 생성
    session = boto3.Session(region_name=region_name)
    
    # DynamoDB 클라이언트 생성
    dynamodb = session.client('dynamodb')
    
    # DynamoDB 테이블 목록 가져오기
    response = dynamodb.list_tables()
    
    print("START")
    # 이름에 키워드가 포함된 테이블 찾기
    for table_name in response.get('TableNames', []):
        if keyword in table_name.lower():  # 소문자로 변환하여 비교
            print(f"\n\n\nFound DynamoDB Table: {table_name}")
            confirmation = input(f"\n\n\nDo you want to delete DynamoDB Table '{table_name}'? (y/n): ").strip().lower()
            if confirmation == 'y':
                print(f"\n\n\nDeleting DynamoDB Table: {table_name}")
                dynamodb.delete_table(TableName=table_name)
    print("\n\n\nEND")

if __name__ == '__main__':
    delete_dynamodb_tables(keyword)
