import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/saket/Downloads/archive (7)/WA_Fn-UseC_-HR-Employee-Attrition.csv")


print("Before cleaning:", df.shape)

# Drop useless columns
df = df.drop(columns=["EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"])

# Convert Attrition Yes/No → 1/0
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# Convert OverTime Yes/No → 1/0
df["OverTime"] = df["OverTime"].map({"Yes": 1, "No": 0})

print("After cleaning:", df.shape)
print("\nAttrition column:\n", df["Attrition"].value_counts())
print("\nAny nulls?", df.isnull().sum().sum())

# Save cleaned data
df.to_csv("hr_cleaned.csv", index=False)
print("\n✅ Cleaned data saved to hr_cleaned.csv")
#            ANALYSIS
# ================================================

# 1. Overall Attrition Rate
total = len(df)
left = int(df["Attrition"].sum())
stayed = (total) - (left)
rate = round((left / total) * 100, 2)

print("==========================================")
print(f"  Total Employees     : {total}")
print(f"  Employees Left      : {left}")
print(f"  Employees Stayed    : {stayed}")
print(f"  Attrition Rate      : {rate}%")
print("==========================================")

# 2. Attrition by Department
print("\n📌 Attrition by Department:")
dept = df.groupby("Department")["Attrition"].mean() * 100
print(dept.round(2))

# 3. Attrition by OverTime
print("\n📌 Attrition by OverTime:")
ot = df.groupby("OverTime")["Attrition"].mean() * 100
print(ot.round(2))

# 4. Attrition by Job Satisfaction
print("\n📌 Attrition by Job Satisfaction:")
js = df.groupby("JobSatisfaction")["Attrition"].mean() * 100
print(js.round(2))

# 5. Attrition by Work Life Balance
print("\n📌 Attrition by Work Life Balance:")
wlb = df.groupby("WorkLifeBalance")["Attrition"].mean() * 100
print(wlb.round(2))

# 6. Attrition by Age Group
df["AgeGroup"] = pd.cut(df["Age"], bins=[18,25,35,45,60],
                        labels=["18-25","26-35","36-45","46-60"])
print("\n📌 Attrition by Age Group:")
age = df.groupby("AgeGroup")["Attrition"].mean() * 100
print(age.round(2))

# 7. Attrition by Income Group
df["IncomeGroup"] = pd.cut(df["MonthlyIncome"],
                           bins=[0,3000,6000,10000,20000],
                           labels=["Low","Medium","High","Very High"])
print("\n📌 Attrition by Income Group:")
inc = df.groupby("IncomeGroup")["Attrition"].mean() * 100
print(inc.round(2))



# Set style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

# ── Chart 1: Overall Attrition Rate (Pie Chart) ──
labels = ["Stayed", "Left"]
sizes = [stayed, left]
colors = ["#2ecc71", "#e74c3c"]

plt.figure()
plt.pie(sizes, labels=labels, colors=colors,
        autopct="%1.1f%%", startangle=90)
plt.title("Overall Attrition Rate")
plt.savefig("chart1_attrition_rate.png")
plt.show()
print("✅ Chart 1 saved")

# ── Chart 2: Attrition by Department ──
plt.figure()
dept_data = df.groupby("Department")["Attrition"].mean() * 100
sns.barplot(x=dept_data.index, y=dept_data.values, palette="Reds_r")
plt.title("Attrition Rate by Department (%)")
plt.xlabel("Department")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart2_department.png")
plt.show()
print("✅ Chart 2 saved")

# ── Chart 3: Attrition by OverTime ──
plt.figure()
ot_data = df.groupby("OverTime")["Attrition"].mean() * 100
sns.barplot(x=["No OverTime", "OverTime"], y=ot_data.values, palette="Oranges_r")
plt.title("Attrition Rate by OverTime (%)")
plt.xlabel("OverTime")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart3_overtime.png")
plt.show()
print("✅ Chart 3 saved")

# ── Chart 4: Attrition by Age Group ──
plt.figure()
age_data = df.groupby("AgeGroup")["Attrition"].mean() * 100
sns.barplot(x=age_data.index.astype(str), y=age_data.values, palette="Blues_r")
plt.title("Attrition Rate by Age Group (%)")
plt.xlabel("Age Group")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart4_agegroup.png")
plt.show()
print("✅ Chart 4 saved")

# ── Chart 5: Attrition by Job Satisfaction ──
plt.figure()
js_data = df.groupby("JobSatisfaction")["Attrition"].mean() * 100
sns.barplot(x=js_data.index, y=js_data.values, palette="Purples_r")
plt.title("Attrition Rate by Job Satisfaction (1=Low, 4=High)")
plt.xlabel("Job Satisfaction")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart5_jobsatisfaction.png")
plt.show()
print("✅ Chart 5 saved")

# ── Chart 6: Attrition by Work Life Balance ──
plt.figure()
wlb_data = df.groupby("WorkLifeBalance")["Attrition"].mean() * 100
sns.barplot(x=wlb_data.index, y=wlb_data.values, palette="Greens_r")
plt.title("Attrition Rate by Work Life Balance (1=Low, 4=High)")
plt.xlabel("Work Life Balance")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart6_worklifebalance.png")
plt.show()
print("✅ Chart 6 saved")

# ── Chart 7: Attrition by Income Group ──
plt.figure()
inc_data = df.groupby("IncomeGroup")["Attrition"].mean() * 100
sns.barplot(x=inc_data.index.astype(str), y=inc_data.values, palette="coolwarm")
plt.title("Attrition Rate by Income Group (%)")
plt.xlabel("Income Group")
plt.ylabel("Attrition Rate (%)")
plt.savefig("chart7_incomegroup.png")
plt.show()
print("✅ Chart 7 saved")

print("\n🎉 All charts saved in your project folder!")


df.to_csv("hr_cleaned.csv", index=False)

