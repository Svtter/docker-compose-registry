#!/usr/bin/env python3
import subprocess
import datetime

def is_registry_running():
    try:
        result = subprocess.run(
            ['docker', 'ps', '--filter', 'name=docker_registry', '--format', '{{.Names}}'],
            capture_output=True,
            text=True
        )
        return 'docker_registry' in result.stdout
    except Exception as e:
        print(f"检查服务状态时发生错误: {e}")
        return False

def stop_registry():
    try:
        subprocess.run(['docker-compose', 'down'], check=True)
        print(f"[{datetime.datetime.now()}] Docker registry 服务已停止")
    except Exception as e:
        print(f"停止服务时发生错误: {e}")

def main():
    if is_registry_running():
        print(f"[{datetime.datetime.now()}] 发现 Docker registry 正在运行，准备停止...")
        stop_registry()
    else:
        print(f"[{datetime.datetime.now()}] Docker registry 未运行")

if __name__ == "__main__":
    main()
