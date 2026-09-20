DOCUMENT OF UNDERSTANDING
EDI - SAP SD Functional Knowledge Transfer
Schaeffler / SAP EP1 customer-EDI processes
FUNCTIONAL KT REFERENCE | SAP SD / EDI / IDOC
Prepared for Document purpose
Primary source Supporting source Status SAP SD Senior Consultant (5+ years experience)
Consolidated understanding of EDI business processes, 
IDoc flow, monitoring and functional ownership
edip1.pdf - EDI supported business processes overview
edip2.pdf - EDI KT session transcript
Working DoU / KT handover reference
Source boundary: This document consolidates information explicitly presented in the supplied KT deck and 
transcript. Customer-specific mappings, configuration details, exact job schedules, and production support 
procedures not present in the source material are intentionally not invented here.Document of Understanding - EDI / SAP SD | 1
EDI | SAP SD Knowledge Transfer | Internal KT Reference
Document Control
Item Value
Document type Document of Understanding (DoU)
Domain SAP SD - Customer EDI
System focus SAP EP1 and associated EDI subsystem
Audience SAP SD / EDI functional consultants, application support 
and KT recipients
Confidentiality Internal KT reference - source presentation is marked 
INTERNAL
Source set edip1.pdf (17 pages) + edip2.pdf (9-page transcript)
How to Use This DoU
Use this document as a functional orientation and troubleshooting reference when analysing customer EDI flows in 
SAP SD. It is deliberately structured from a consultant perspective: business process first, message/interface second, 
IDoc lifecycle third, and operational support last.
Contents
 1. Executive Summary
 2. EDI Fundamentals
 3. Business Processes and Message Types
 4. SAP EP1 and EDI Architecture
 5. IDoc Structure and Lifecycle
 6. Inbound DELINS / Schedule Agreement Flow
 7. Outbound ASN / SHPMNT Flow
 8. Customer Guidelines and Mapping Considerations
 9. Monitoring and Error Handling
 10. Functional Ownership and Ticket Routing
 11. SAP SD Consultant Working Model
 12. KT Outcomes, Open Points and Validation Checklist
 Appendix A - Quick Reference Matrix
 Appendix B - Source TraceabilityDocument of Understanding - EDI / SAP SD | 2
EDI | SAP SD Knowledge Transfer | Internal KT Reference
1. Executive Summary
Electronic Data Interchange (EDI) is presented in the KT material as the electronic transmission of business processes 
between computer systems using an agreed standard for structuring data or messages. The operational goal is to 
exchange routine business documents such as orders, invoices and delivery schedules between customer and supplier
systems without repeated manual data entry.
For the SAP SD landscape described in the KT, customer EDI connects external customer messages to SAP EP1 through 
an EDI subsystem and transformation layer. The SAP-side representation is an IDoc, which carries control 
information, application data and processing status. Customer-specific formats are transformed into SAP IDoc 
structures on inbound flows, while outbound IDocs are transformed into customer-specific EDI formats for 
transmission.
What a senior SAP SD functional consultant should retain
 Understand the business document behind each message type before troubleshooting the technical message.
 Read an IDoc through control record, data records and status records; status progression explains where processing 
stopped.
 Customer guidelines are essential because customer-specific fields, qualifiers and conventions can differ even when a 
common EDI standard is used.
 For support, distinguish SAP application errors from EDI transformation/transport issues and route the incident to the
correct regional functional EDI team.
2. EDI Fundamentals
2.1 Definition and Business Value
The source defines EDI as the electronic transmission of business processes between computer systems using an 
agreed standard for structuring data or messages. The presentation highlights fast transmission, improved accuracy / 
fewer data-entry errors, and reduced transaction costs as key advantages (edip1.pdf, pp. 3-4).
2.2 Common Message Standards Mentioned
Standard / Format Source description / usage
ANSI X12
Standard defined by the American National Standards 
Institute; the KT specifically references ST830 in the North 
American context.
EDIFACT
International standard defined by the United Nations; 
examples are shown for delivery schedule / forecast-style 
messages.
VDA
Automotive-industry standard; VDA 4905 is presented as a 
forecast release standard from the German Automotive 
Association.
ODETTE Industry-specific standard used mainly in Europe; customer
examples are shown in the KT materials.
RND
Fixed-length format discussed in the transcript; the exact 
customer-specific structure must be read from the 
applicable guideline.
Functional point: The transcript stresses that knowing only the generic EDI standard is not enough. The 
consultant must read the customer guideline because the customer defines which field / element carries which 
business information and may add customer-specific conventions.Document of Understanding - EDI / SAP SD | 3
EDI | SAP SD Knowledge Transfer | Internal KT Reference
2.3 Why Customer Guidelines Matter
The KT explains that the consultant needs the customer implementation guideline to identify the business meaning of 
segments, qualifiers and fields. Examples discussed include article/material numbers, customer material numbers and
PO references. The transcript also gives an example where a customer-specific additional value is not part of the 
generic standard and therefore must be handled according to that customer document (edip2.pdf, transcript pages 2-
3).
3. Business Processes and Message Types
The customer-EDI supported processes presented in the deck cover scheduling-agreement releases, consignment 
processes, sales orders and changes, sales-order confirmations, advanced shipping notifications, invoices, customer 
self-billing and technical / application acknowledgements (edip1.pdf, p. 9).
IDoc / Message Type Direction Business process in source Functional understanding
DELINS / EDLNOT INB Forecast / JIT release posted to 
scheduling agreement
Inbound customer release 
updates scheduling / delivery 
requirements.
ORDERS / ORDCHG INB Sales order creation and change Creates or changes sales-order 
demand in SAP.
ORDRSP OUTB Sales order confirmation
Returns confirmation / 
confirmed quantities and dates 
to customer.
SHPMNT OUTB Advanced Shipping Notification 
(ASN)
Communicates shipment / 
delivery information to 
customer.
INVOIC OUTB Customer sales invoices Sends billing / invoice 
information to customer.
SBWAP INB Customer self-billing invoice Receives customer-generated 
self-billing information.
STATUS INB Technical / functional / 
application acknowledgement
Provides status / 
acknowledgement information 
for message processing.
WSW / SPEEDI INB
Monitoring-oriented 
information; technical / 
functional acknowledgement, 
goods receipt, text / routing 
information
Referenced especially for US 
customers using ANSI X12 
message types.
3.1 Scheduling Agreement: Forecast vs Shipping Schedule
The transcript distinguishes longer-term forecast information from direct shipping demand. Forecast information 
supports planning and can represent a monthly demand, while a shipping schedule expresses a more immediate 
requirement such as quantities required on specific dates. The session describes schedule-agreement variants 
including a standard type, ESP (external service provider / consignment process), and Schaeffler-specific variants 
(edip2.pdf, transcript page 4).
Example from the KT discussion
 Forecast: planning-oriented demand over a longer horizon.
 Shipping schedule: date-specific demand that drives a near-term shipping requirement.
 An inbound release can fail when the customer introduces a material that is not yet prepared on the SAP side; this 
becomes an application / preparation issue rather than simply a transport issue.Document of Understanding - EDI / SAP SD | 4
EDI | SAP SD Knowledge Transfer | Internal KT Reference
3.2 Order Confirmation
The session explains that confirmed quantities may be split across delivery dates. The resulting sales order 
confirmation is sent outbound using the IDoc order-response process, returning confirmation information to the 
customer (edip2.pdf, transcript page 5).
3.3 ASN / Shipment Notification
For automotive customers, the shipping advice / shipping notification is used to communicate when goods are 
expected to arrive at the customer plant. The session describes transport / consignment terminology and distinguishes 
an individual consignment shipment from a truck load containing multiple consignments (edip2.pdf, transcript page 
5).
4. SAP EP1 and EDI Architecture
The deck presents a pre-merger Schaeffler landscape in which customer EDI connects external partners to SAP 
systems through an EDI subsystem. The EDI subsystem shown is Axway TradeSync Integration Manager (TSIM), with 
an IBIS platform used in the message-processing flow. The presentation states that customer-specific EDIFACT, VDA, 
ODETTE, RND and ANSI X12 formats are transformed into SAP IDocs on inbound processing and transformed from 
SAP IDocs to external formats for outbound processing.
Customer ERP External EDI format Axway TSIM / IBIS SAP EP1 IDoc SAP SD business
document
↓ ↓ ↓ ↓ ↓
The deck gives an example of a direct shipment process involving customer EDI messages such as ORDERS, ORDRSP, 
DESADV and INVOIC / self-billing, with SAP EP1 at the center of the application processing and the EDI subsystem 
acting as the integration boundary (edip1.pdf, p. 10).
4.1 Scale and Partner Context
Partner category Volumes described in presentation Context
Customers ~1,000 Schaeffler customers; ~300 
Schaeffler VLS customers Mostly automotive / industry
Suppliers ~12 direct; ~800 via SupplyOn 
marketplace External supplier ecosystem
Carriers ~20 Carrier integration
Warehouses ~8 Warehouse interfaces
4.2 Functional Interpretation for SAP SD
For an SAP SD consultant, the important boundary is: external format and transport are handled outside the SAP 
application layer, while SAP SD owns the interpretation and application processing once the message has been 
represented as an IDoc. The consultant therefore needs enough EDI knowledge to trace the message into SAP, but 
should not assume every failure is an SD configuration defect.
5. IDoc Structure and Lifecycle
The KT explicitly breaks the SAP in-house IDoc structure into three logical parts: control record, data records and 
status records.Document of Understanding - EDI / SAP SD | 5
EDI | SAP SD Knowledge Transfer | Internal KT Reference
IDoc part What it contains Functional use
Control record
Administrative information such as 
IDoc number, sender, receiver and 
IDoc type
Confirms who sent the message, who 
receives it, and which message / IDoc 
definition is involved.
Data records Segments containing 
application/business data
Read the actual customer, order, 
material, quantity and reference 
information carried by the message.
Status records Processing history / current status
Shows what happened to the IDoc, 
where processing stopped and 
whether application posting 
succeeded.
5.1 Reading an IDoc as a Functional Consultant
The transcript demonstrates a practical reading approach: identify the segment and qualifier, interpret the business 
value, and then confirm the status history. Examples discussed include seller details, article / material information, 
customer material number and PO references. For troubleshooting, status progression is used to determine whether 
the IDoc was merely received, picked up for processing, successfully posted or stopped in error (edip2.pdf, transcript 
pages 6-7).
Key status concepts captured in the source
 Status 64: IDoc is received / waiting for processing job in the inbound flow.
 Status 53: successful application posting is demonstrated in the example after processing.
 Status records should be read as a sequence to locate the processing point of failure.
6. Inbound DELINS / Schedule Agreement Flow
The inbound flow shown in the deck starts with an external customer EDI message entering the EDI subsystem. The 
message is transformed into an SAP IDoc. SAP uses the partner-profile-driven processing configuration, then executes 
pre-check logic and application processing before updating the scheduling agreement / related SAP data.
Customer
release
Axway
TSIM / IBIS
SAP IDoc
received
Status 64 Processing
job
Pre-checks /
BAdI / exits
SAP
application
posting
Scheduling
agreement
update
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Step Source detail Consultant focus
1. Receive IDoc posted with status 64 Confirm IDoc arrival and sender / 
receiver.
2. Determine processing
Processing code from WE20 is 
referenced; examples include ZDEL / 
WSW-SPEEDI_DELI
Validate partner/message configuration 
and expected processing path.
3. Pre-check
Extensions / standard-field adjustments 
are performed before standard 
processing
Check whether data preparation / 
validation changes the incoming payload.
4. SAP processing SAP standard function module is used; 
BAdIs and user exits may be fully used
Analyse application messages and 
custom enhancement logic.
5. Error handling ZVDELMON is named for error handling Use the designated monitor to isolate 
application-level errors.
6. Update Scheduling agreement release is updated 
after successful processing
Validate that business data reflects the 
incoming release.Document of Understanding - EDI / SAP SD | 6
EDI | SAP SD Knowledge Transfer | Internal KT Reference
Important operational caveat: The transcript notes that some releases cannot be processed fully automatically 
because a customer may send a new material that is not yet prepared on the SAP side. The consultant should 
therefore distinguish a valid EDI transport from a valid business-master-data setup.
7. Outbound ASN / SHPMNT Flow
The outbound ASN process starts from shipment loading and creates an SHPMNT IDoc. The deck shows pre-check 
processing, customer-specific adjustments through BAdIs / user exits, and then transformation through the EDI 
subsystem before the message is delivered to the customer.
Shipment
loading
Pre-checks Create
SHPMNT IDoc
Postprocessing /
exits
Axway TSIM /
IBIS
Customer EDI
format
Customer
↓ ↓ ↓ ↓ ↓ ↓ ↓
Element Source detail Functional focus
Trigger Shipment loading / completion; endstatus 7 shown
Confirm the business event that should 
create the ASN.
Message SHPMNT / SHPMNTO5 is shown Validate the expected shipment IDoc 
type.
Pre-check ZL0x-related pre-check functions and 
table ZVFBSTN_OUT are shown
Check outbound preparation / custom 
field logic.
Processing codes SD11, ZSD11, WSW/SPEEDI_SHPM are 
referenced
Confirm the processing path when 
analysing failures.
Enhancements BAdIs and user exits are stated as fully 
used
Check custom logic before assuming 
standard SD behaviour.
Transformation Axway TSIM / IBIS converts the SAP 
representation to customer formats
If SAP IDoc is successful but no external 
EDI arrives, the issue may be 
downstream of SAP.
8. Customer Guidelines and Mapping Considerations
The transcript repeatedly emphasizes that EDI implementation is customer-specific even when the underlying format 
is a published standard. The customer guideline is therefore a primary functional specification for understanding 
which information is transmitted in which segment / element.
8.1 Practical Reading Method
Question What business document is this? Who is the trading partner? What does the segment mean? Which material / reference is involved? Is the field standard or customer-specific? Where did processing stop? What to inspect
Message type + customer process: forecast, order, 
confirmation, ASN, invoice, acknowledgement, etc.
Sender / receiver in IDoc control record and partner profile 
context.
Segment name + qualifier + customer guideline description.
Material number, customer material number, PO / release 
reference and other key business identifiers.
Compare the guideline against the generic standard; do not 
assume a customer addition is globally standard.
Read IDoc status history from receipt through application 
posting.Document of Understanding - EDI / SAP SD | 7
EDI | SAP SD Knowledge Transfer | Internal KT Reference
8.2 Consultant Principle
The source material advises using standard fields wherever possible and avoiding unnecessary custom enhancements.
This is a design principle captured from the KT session, not a complete development standard or approval policy.
9. Monitoring and Error Handling
The presentation includes SAP EP1 monitors for incoming forecast / delivery schedule information and incoming 
orders. The operational objective is to see the message, sender, date, message type, IDoc number and the error / 
processing state so that functional support can act on the correct business document.
9.1 Suggested Functional Triage Sequence
Sequence Functional check Outcome
1 Identify message type and direction Establish the business process and expected
flow.
2 Check control record Confirm sender, receiver, IDoc type and 
IDoc number.
3 Read data records Identify affected material, order, release, 
shipment or invoice data.
4 Read status records Locate the last successful step and first 
error / waiting condition.
5 Validate master / transactional readiness
For example, confirm that new customer 
materials / required SAP setup are 
prepared.
6 Check enhancement / pre-check path Review BAdI, user-exit or pre-check logic 
referenced for the message.
7 Assess downstream integration
If SAP processing is successful but external 
delivery is missing, check the EDI 
subsystem / transformation path.
8 Route / document Use the regional EDI ownership model and 
attach the key message identifiers.
Support evidence to capture in a ticket
 IDoc number and message type
 Sender / customer and creation date
 Relevant business document / order / release / shipment reference
 Last successful status and first error status
 Exact error text / monitor evidence
 Whether SAP application posting occurred
10. Functional Ownership and Ticket Routing
The source deck states that regional Customer-EDI teams support their region and that the pre-merger ServiceNow 
setup uses regional assignment groups. The document also notes that organizational changes were expected, so the 
exact current assignment groups should be validated before production use.
Area / Region Assignment group shown in source Scope / note
Europe, Africa and EDI global SALES_R3S_EDI Customer-EDI and global sales EDI 
context.
Americas EDI_ECOMMERCE_AO_R_AM/
SD_LOGISTICS_BAM_R_AM Regional customer-EDI support context.
China EDI_ECOMMERCE_AO_R_GC Regional customer-EDI support context.
Asia Pacific EDI_ECOMMERCE_AO_R_AP Regional customer-EDI support context.Document of Understanding - EDI / SAP SD | 8
EDI | SAP SD Knowledge Transfer | Internal KT Reference
10.1 Functional Customer-EDI Team
The deck lists a functional Customer-EDI team distributed across Germany, Poland, the USA and Canada, with 
responsibility aligned to systems / regions. The session explains that responsibility is regional even though the support
model is being consolidated after the merger. The names shown in the source should be treated as a point-in-time KT 
reference rather than a current on-call roster.
10.2 Related Interface Ownership
The source allocation slide separates Customer-EDI, Intercompany-EDI, SCM-EDI, Logistics-EDI and FI-EDI. For SAP SD 
support, the most directly relevant categories are Customer-EDI and Intercompany-EDI; other areas may be involved 
when the business process crosses procurement, warehouse, carrier or finance interfaces.
11. SAP SD Consultant Working Model
11.1 Business-first Troubleshooting
Start with the business event: What was the customer trying to send or receive? Then map that event to the message 
type, IDoc, SAP application document and status. This prevents a technical symptom from being analysed without 
understanding the business transaction it represents.
11.2 Functional Questions to Ask
 What customer and region are involved?
 Is the message inbound or outbound?
 What is the expected SAP SD business document?
 Which message / IDoc type is expected?
 What references identify the business transaction?
 At which IDoc status did processing stop?
 Did the message fail before or after SAP application posting?
 Is the issue standard processing, customer-specific enhancement, master data, or downstream EDI 
transformation?
 What customer guideline defines the field / segment that is disputed?
11.3 Scenario-Based Understanding
Scenario Likely investigation path from source
Inbound release not posted
Check IDoc receipt / status 64 -> processing job -> processing 
code / partner configuration -> pre-check / enhancement -> 
application error -> required master-data readiness.
Order confirmation not received by customer
Check SAP application confirmation -> outbound ORDRSP IDoc 
-> outbound status -> EDI subsystem transformation / 
transmission.
ASN not received
Check shipment event -> SHPMNT IDoc creation -> outbound 
processing codes / exits -> Axway TSIM / IBIS transformation -> 
customer delivery.
Customer sends unsupported / unexpected material Confirm material setup / preparation in SAP; source explicitly 
notes this can prevent fully automatic processing.
Field meaning unclear Use the customer implementation guideline and compare the 
segment + qualifier + transmitted value.Document of Understanding - EDI / SAP SD | 9
EDI | SAP SD Knowledge Transfer | Internal KT Reference
12. KT Outcomes, Open Points and Validation Checklist
12.1 KT Outcomes
 Understand the purpose of EDI and the role of published vs customer-specific formats.
 Recognize the main customer-EDI business processes supported in SAP EP1.
 Read an SAP IDoc using control, data and status records.
 Understand the inbound DELINS and outbound SHPMNT processing patterns presented in the KT.
 Recognize the functional importance of customer guidelines and qualifiers.
 Use the regional support model for escalation / ticket routing.
12.2 Open Points for a Follow-on KT / Validation
Open point Exact current post-merger system / team ownership Current partner profiles and processing codes
Job names / schedules Customer-specific mappings Current ServiceNow assignment groups Detailed error catalogue Why it should be validated
The source is explicitly described as a pre-merger setup and 
mentions upcoming organizational changes.
The KT shows examples such as ZDEL, SD11, ZSD11 and 
WSW/SPEEDI variants, but not a complete configuration 
matrix.
The source states that jobs process inbound IDocs but does not 
provide a complete operational schedule.
The deck provides examples but not a complete mapping 
specification per customer / format.
The slide labels the structure as pre-merger; current ownership
should be checked before using the listed groups.
Monitors and error handling are shown, but a complete 
application-error catalogue is outside the supplied source.
12.3 KT Completion Checklist
Topic EDI concepts and standards Business process / message matrix IDoc structure and status flow Inbound DELINS flow Outbound SHPMNT / ASN flow Customer guideline interpretation Monitoring and error handling Regional ownership / ticket routing Understanding achieved ☐
☐
☐
☐
☐
☐
☐
☐Evidence / follow-up
Document of Understanding - EDI / SAP SD | 10
EDI | SAP SD Knowledge Transfer | Internal KT Reference
Appendix A - Quick Reference Matrix
Message Dir. Business purpose Key source artefacts / 
checkpoints
DELINS / EDLNOT INB Forecast / JIT release / 
scheduling agreement update
Status 64 -> job -> processing 
code -> pre-check -> SAP 
application -> update
ORDERS / ORDCHG INB Sales order create / change Customer order -> IDoc -> 
application document
ORDRSP OUTB Sales order confirmation Confirmed quantity / dates -> 
outbound IDoc -> customer
SHPMNT OUTB ASN / shipment notification Shipment loading -> SHPMNT -> 
transformation -> customer
INVOIC OUTB Customer sales invoice SAP billing -> invoice EDI output
SBWAP INB Customer self-billing invoice Customer self-billing -> inbound
SAP processing
STATUS INB Technical / functional / 
application acknowledgement
Acknowledgement and message 
status
WSW / SPEEDI INB Monitoring / acknowledgement /
goods receipt / routing context
Mainly cited for US ANSI X12 
customers
Appendix B - Source Traceability
The following traceability map identifies where the main content of this DoU originates in the supplied material. Page 
references below refer to the supplied PDF page numbers; transcript references are by transcript page and the 
timestamped discussion where available.
DoU section Primary source location What was taken from the source
EDI definition / standards edip1.pdf pp. 3-6; edip2.pdf transcript pp. 1-
3
EDI definition, benefits, ANSI X12, EDIFACT, 
VDA, ODETTE, RND, customer-guideline 
importance.
Business processes edip1.pdf p. 9; edip2.pdf transcript pp. 4-6
Customer-EDI message types, scheduling 
agreements, forecast vs shipping schedule, 
order confirmation, ASN / consignment 
context.
Architecture edip1.pdf pp. 7-10
Axway TSIM, SAP landscape, customer / 
supplier / carrier / warehouse context, 
direct shipment example.
IDoc structure edip1.pdf pp. 11-13; edip2.pdf transcript pp. 
6-7
Control / data / status records, inbound 
DELINS and outbound SHPMNT processing 
flows, processing codes and enhancement 
points.
Support / ownership edip1.pdf pp. 14-17; edip2.pdf transcript pp. 
7-9
Functional EDI team, regional support 
model, ServiceNow groups, allocation of 
tasks, monitoring.
Validation note: The supplied transcript contains transcription artefacts and some terms are difficult to read. 
Where the transcript was unclear, this DoU preserves the wording shown in the source or stays at the level 
supported by the presentation rather than silently normalizing it.
End of Document
EDI / SAP SD Functional KT - DoU
Prepared as a working knowledge-transfer reference from the supplied source materials.Document of Understanding - EDI / SAP SD | 
