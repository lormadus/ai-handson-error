PS C:\Users\Admin\RAGproj50932340\src> python get_product_documents.py --query "I need a new tent for 4 people, what would you recommend?"    
Traceback (most recent call last):
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 123, in <module>
    result = get_product_documents(messages=[{"role": "user", "content": query}])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
    result = get_product_documents(messages=[{"role": "user", "content": query}])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 55, in get_product_documents
    intent_mapping_response = chat.complete(
                              ^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\site-packages\azure\ai\inference\_patch.py", line 738, in complete
    raise HttpResponseError(response=response)
azure.core.exceptions.HttpResponseError: (None) Invalid URL (POST /v1/chat/completions)
Code: None
Message: Invalid URL (POST /v1/chat/compython get_product_documents.py --query "I need a new tent for 4 people, what would you recommend?"
Traceback (most recent call last):
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 119, in <module>
    result = get_product_documents(messages=[{"role": "user", "content": query}])
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 51, in get_product_documents
    intent_mapping_response = chat.complete(
                              ^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\site-packages\azure\ai\inference\_patch.py", line 738, in complete
    raise HttpResponseError(response=response)
azure.core.exceptions.HttpResponseError: (None) Invalid URL (POST /v1/chat/completions)
Code: None
Message: Invalid URL (POST /v1/chat/completions)










PS C:\Users\Admin\RAGproj50932340\src> python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?"
Traceback (most recent call last):
  File "C:\Users\Admin\RAGproj50932340\src\chat_with_products.py", line 65, in <module>
    response = chat_with_products(messages=[{"role": "user", "content": args.query}])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\chat_with_products.py", line 29, in chat_with_products
    documents = get_product_documents(messages, context)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 51, in get_product_documents
    intent_mapping_response = chat.complete(
                              ^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\site-packages\azure\ai\inference\_patch.py", line 738, in complete
    raise HttpResponseError(response=response)
azure.core.exceptions.HttpResponseError: (None) Invalid URL (POST /v1/chat/completions)
Code: None
Message: Invalid URL (POST /v1/chat/completions)
PS C:\Users\Admin\RAGproj50932340\src> ^C
PS C:\Users\Admin\RAGproj50932340\src> python chat_with_products.py --query "I need a new tent for 4 people, what would you recommend?"       
Successfully created AI Project client
Successfully created chat and embeddings clients
Successfully retrieved search connection
Successfully created search client
Traceback (most recent call last):
  File "C:\Users\Admin\RAGproj50932340\src\chat_with_products.py", line 65, in <module>
    response = chat_with_products(messages=[{"role": "user", "content": args.query}])
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\chat_with_products.py", line 29, in chat_with_products
    documents = get_product_documents(messages, context)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Admin\RAGproj50932340\src\get_product_documents.py", line 89, in get_product_documents
    intent_mapping_response = chat.complete(
                              ^^^^^^^^^^^^^^
  File "C:\Users\Student\miniconda3\Lib\site-packages\azure\ai\inference\_patch.py", line 738, in complete
    raise HttpResponseError(response=response)
azure.core.exceptions.HttpResponseError: (None) Invalid URL (POST /v1/chat/completions)
Code: None
Message: Invalid URL (POST /v1/chat/completions)
‌‌
