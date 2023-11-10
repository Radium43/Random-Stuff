#include <iostream>
#include <iomanip>
#include <Windows.h>
#include <Psapi.h>
#include <Pdh.h>

#pragma comment(lib, "pdh.lib")

void printError(const char* message) {
    std::cerr << "Error: " << message << " (Error code: " << GetLastError() << ")\n";
}

double calculateCPUPercentage(ULONGLONG idleTicks, ULONGLONG totalTicks) {
    static ULONGLONG prevTotalTicks = 0;
    static ULONGLONG prevIdleTicks = 0;

    ULONGLONG totalTicksSinceLastTime = totalTicks - prevTotalTicks;
    ULONGLONG idleTicksSinceLastTime = idleTicks - prevIdleTicks;

    double result = 100.0 - ((idleTicksSinceLastTime * 100.0) / totalTicksSinceLastTime);

    prevTotalTicks = totalTicks;
    prevIdleTicks = idleTicks;

    return result;
}

void monitorSystem() {
    PDH_HQUERY cpuQuery;
    PDH_HCOUNTER cpuTotalCounter;
    ULONGLONG lastIdleTime, lastKernelTime, lastUserTime;

    PdhOpenQuery(NULL, NULL, &cpuQuery);
    PdhAddCounter(cpuQuery, L"\\Processor(_Total)\\% Processor Time", NULL, &cpuTotalCounter);
    PdhCollectQueryData(cpuQuery);

    MEMORYSTATUSEX memoryStatus;
    memoryStatus.dwLength = sizeof(memoryStatus);

    while (true) {
        PDH_FMT_COUNTERVALUE counterVal;
        PdhCollectQueryData(cpuQuery);
        PdhGetFormattedCounterValue(cpuTotalCounter, PDH_FMT_DOUBLE, NULL, &counterVal);
        double cpuUsage = counterVal.doubleValue;
        GlobalMemoryStatusEx(&memoryStatus);
        double ramUsage = static_cast<double>(memoryStatus.dwMemoryLoad);
        ULARGE_INTEGER freeBytes, totalBytes, totalFreeBytes;
        GetDiskFreeSpaceEx(L"C:\\", NULL, &totalBytes, &freeBytes);
        totalFreeBytes.QuadPart = freeBytes.QuadPart + totalBytes.QuadPart;
        double diskUsage = ((totalFreeBytes.QuadPart - freeBytes.QuadPart) / static_cast<double>(totalFreeBytes.QuadPart)) * 100.0;

        std::cout << "\rCPU Usage: " << std::setw(6) << std::fixed << std::setprecision(2) << cpuUsage << "%"
            << " | RAM Usage: " << std::setw(6) << std::fixed << std::setprecision(2) << ramUsage << "%"
            << " | Disk Usage: " << std::setw(6) << std::fixed << std::setprecision(2) << diskUsage << "%";
        Sleep(1000);
    }
}

int main() {
    monitorSystem();
    return 0;
}
