#!/usr/bin/env python3
"""
测试脚本：验证新版OpenAI兼容API配置
支持OpenAI、千问等兼容模型的统一调用
"""

import sys
import os
sys.path.append('.')

try:
    from utils import openai_api_key, openai_base_url
    from persona.prompt_template.gpt_structure import ChatGPT_request, GPT4_request, get_embedding
    
    print("🚀 开始测试OpenAI兼容API配置...")
    print(f"API Key: {openai_api_key[:20]}...")
    print(f"Base URL: {openai_base_url}")
    
    # 测试Chat模型
    print("\n💬 测试Chat模型...")
    test_prompt = "你好，请用中文简单介绍一下人工智能。限制在50字以内。"
    
    try:
        response = ChatGPT_request(test_prompt)
        print(f"✅ Chat模型响应成功:")
        print(f"响应内容: {response}")
    except Exception as e:
        print(f"❌ Chat模型测试失败: {e}")
    
    # 测试高级模型
    print("\n🤖 测试高级模型...")
    test_prompt_advanced = "What is AI? Answer in one sentence."
    
    try:
        response = GPT4_request(test_prompt_advanced)
        print(f"✅ 高级模型响应成功:")
        print(f"响应内容: {response}")
    except Exception as e:
        print(f"❌ 高级模型测试失败: {e}")
    
    # 测试嵌入功能
    print("\n🔗 测试嵌入功能...")
    test_text = "这是一个测试文本"
    
    try:
        embedding = get_embedding(test_text)
        print(f"✅ 嵌入功能正常，向量维度: {len(embedding)}")
        print(f"向量前5个元素: {embedding[:5]}")
    except Exception as e:
        print(f"❌ 嵌入功能测试失败: {e}")
    
    print("\n🎉 API测试完成！")
    print("\n📋 配置说明:")
    print("- 统一使用OpenAI兼容格式的API调用")
    print("- 支持通过修改utils.py轻松切换不同模型服务")
    print("- 千问模型切换：只需修改base_url和模型名称")
    print("- 当前支持的模型类型：Chat、高级推理、文本嵌入")
    
except ImportError as e:
    print(f"❌ 导入错误: {e}")
    print("请确保在正确的目录下运行此脚本")
except Exception as e:
    print(f"❌ 测试过程中出现错误: {e}")
