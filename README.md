SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
Document of Understanding (DOU)
SAP SD Functional Support | EAEDI Special Processes and Sales Order 
Integration
Document status Draft for functional validation
Audience SAP SD Senior Functional Consultants / EAEDI 
Support
Knowledge-transfer presenters Monika Roegele (Consignment & DON); Sven 
Hildebrand (Sales Orders)
Source material Provided KT transcript excerpts and five 
presentation screenshots
Prepared on 24 October 2026
1. Executive Understanding
The sessions explain Schaeffler-specific EAEDI processing beyond standard SAP SD: external 
consignment stock and its EDLNOT reconciliation, customer-specific delivery order number 
(DON/Kanban) handling, and inbound sales orders/order changes with outbound confirmations. 
Support must distinguish EDI mapping/IDoc failures from business data, stock, scheduling 
agreement, and delivery execution issues.
2. Process Landscape
Area Main SAP object / message Key business outcome
Consignment Consignment scheduling 
agreement; EDLNOT 30/35/36
Stock, withdrawal and billing 
reconciliation
DON / Kanban Special scheduling agreement 
(ZV87 per slide); JIT / 
ZDELFOR1
Preserve customer 
Kanban/pickup identifiers 
through delivery and ASN
Sales orders ORDERS04; order and order-
change messages
Correct partner 
determination, tolerance 
controls and confirmations
3. Consignment Process (EDL)
3.1 End-to-end business flow
1. Customer transmits DELINS requirements to Schaeffler; goods are delivered to a customer-
operated or third-party consignment warehouse near the customer.
2. Ownership of the consignment inventory remains with Schaeffler until the relevant 
withdrawal/consumption event under the agreed model.
3. Warehouse sends EDLNOT 30 (physical receipt), EDLNOT 35 (stock position; sometimes 35F 
free / 35S blocked), and EDLNOT 36 (goods issue/withdrawal).
4. Schaeffer reconciles the received stock and withdrawal information with SAP stock and the 
scheduling agreement; withdrawal information supports customer invoicing or self-billing 
invoice (SBI) reconciliation. SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
3.2 Functional setup and transactions
 Consignment scheduling agreement has a special stock partner (consignment destination); the 
customer may also operate that location.
 Cumulative quantities include delivered, received, in-transit and withdrawn/issued quantities. A
linked internal sales order can be generated for withdrawal processing.
 ZVEDLMON / ZV EDLMON (presentation spelling: ZVEDLMON): monitor EDLNOT inbound 
consignment messages.
 MB58: display customer consignment stock in SAP.
 /SGD/SD_EDLMON: business EDL cockpit with traffic-light reconciliation, in-transit quantities, 
stock and open postings.
 /SGD/SD_EDI_MINSTOCK: maintain minimum stock demand; special schedule line M may be 
generated (illustrated with 480 pieces).
 OVD0 / Z_VT664A and VA01 order type ZV89: internal sales-order-type definition/setup shown in
presentation; normally onboarding activity, not routine incident handling.
 Cumulative reset and special cumulative values are relevant to consignment scheduling 
agreements; follow customer-specific process before modifying values.
3.3 Customer-specific switches
Customer switch configuration is accessed via SM30 and table/view name that appears as ZBK…SH 
in the transcript; the exact technical name must be verified in the system. Select sold-to party, sales 
organization and validity period. Under the External Service Provider (ESP) warehouse tab, options 
described include adding the order number, overriding the unloading point, overriding customer 
plant, aggregating same-date EDLNOT 35 records, and customer-specific VMI behavior. Do not 
change switches without approved impact analysis.
3.4 Consignment support approach
5. Open the EDL cockpit for the sales responsible or scheduling agreement; review 
red/yellow/green status and stock differences.
6. Compare MB58 stock, cockpit stock, customer-reported EDLNOT 35 stock, cumulative 
deliveries/withdrawals and in-transit quantity.
7. Check last receipt date and completeness of EDLNOT 30/35/36 messages; some customers do not 
send 35 stock reports, so red status may reflect missing stock reporting rather than a posting 
failure.
8. Review message-level processing and warnings in ZVEDLMON; reconcile movements 
chronologically using opening stock + receipts withdrawals ± corrections. −
9. For failed goods issue or missing delivery, validate stock availability, linked sales document and 
IDoc processing; escalate business quantity or missing-customer-message issues with evidence.
4. Delivery Order Number (DON / Kanban)
DON is a customer-specific process in which schedule-line-level Kanban, run, pickup-sheet or 
receiving-point information must be preserved on labels, delivery documents and ASN. Schaeffler 
uses an established customized approach rather than SAP’s newer S/4HANA sequence-JIT process.
4.1 Schedule and message behavior
 The presentation identifies scheduling agreement ZV87 (and related ZV44 processing).
 Special information is usually received in JIT schedules, not forecast schedules; Kanban Detail 
displays identifiers for individual schedule lines. SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
 ZVDELMON displays forecast/JIT messages, including special DON fields; the slide identifies 
ZDELFOR1.
 Customer receiving point may differ by schedule line and must be retained for downstream 
delivery/ASN.
4.2 Kanban types and delivery creation
Type Rule Operational impact
01 One Kanban identifier per 
handling unit
Multiple Kanban numbers 
may be represented within 
one delivery, subject to 
packaging and checks
03 One Kanban identifier per 
delivery note
Do not combine different 
Kanban numbers into one 
delivery
02 Described as no longer in use Verify legacy customers before
any change
Use the dedicated delivery creation transaction ZDON_VL10 / ZDON_VL10 (transcript appears as “set 
on VL10”; verify exact code), which validates compatible Kanban grouping. Creating delivery 
directly from the scheduling agreement may combine open quantities without required DON checks.
The session also references ZV44 packaging/deviating order handling and ZV87 setup in the 
customer-specific switch table; validate exact document type codes before operational use.
4.3 Frequent DON incidents
 ASN fails or lacks DON number: compare delivery, schedule-line Kanban detail and customer 
requirement; a manually added line or over-delivery may have blank Kanban information.
 Missing Kanban Detail button: check customer-specific switch setup, agreement type and 
applicability.
 Delivery combination error: confirm whether Kanban type 01 or 03 applies; recreate delivery 
using validated transaction where necessary.
 Missing or inconsistent receiving-point / pickup-sheet data: check inbound JIT IDoc, schedule-
line fields and delivery transfer.
Important control: do not invent or manually assign a missing Kanban number. Obtain the correct 
identifier from the sales responsible/customer and follow authorized correction and ASN 
reprocessing steps.
5. EAEDI Sales Orders and Order Changes
5.1 Inbound processing
 External customers send purchase orders and changes using ORDERS04 basic type, with 
customer-specific message processing.
 Inbound sales-order errors are reviewed in the EAEDI order monitor (transcript pronunciation 
“CV Ottman / CV Hartmann”; exact SAP transaction must be verified).
 Typical exceptions include duplicate orders already created manually, invalid customer 
material, and IDocs set to status 68 after business intervention.
 One ship-to address per sales order is preferred. Using a document-specific address instead of 
customer master ship-to can prevent expected delivery/shipment consolidation. SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
5.2 Partner determination and master data
 VOE4 / EDPA mapping determines internal sold-to, ship-to and potentially bill-to accounts from 
external EDI partner identifiers; the session also references VOE2 for sales organization 
determination.
 Inbound E1EDKA1 partner segments may include AG (sold-to), LF (vendor) and WE (ship-to). 
External IDs/branch codes map to SAP customer master accounts.
 EDPA and EDSDC are described as required foundational setup for customers using EAEDI sales-
order creation and change processing.
 Customer master must contain valid ship-to, sales area, partner functions, unloading point 
where used, and order expert/contact.
 Order combination settings differ between scheduling agreements and sales orders; confirm 
customer delivery-consolidation requirements.
5.3 Order change, tolerance and confirmation
 Schaeffler-specific tolerance profile is copied to sales-order item at creation, then applied to 
incoming changes in quantity/date. Sales can adjust approved profile per business 
requirements.
 A strict example shown is profile 003 (90 days / 0%); alternative profile values are customer-
specific and require system verification.
 Instead of physically deleting a sales-order item after customer cancellation, Schaeffler can set a 
reason for rejection through customer switch logic.
 Customer PO item reference must remain correct when copying or replacing order items; 
missing reference may block outbound confirmation.
 Order confirmation output is header-level; CVAB is referenced as a multipurpose output type. 
EAEDI, manual EAEDI and internal EAEDI SAP modes are described.
 For unconfirmed quantities, customer-specific dummy/future confirmation dates may be sent 
where EDI requires a date. Such settings are not universal and must be validated.
 Order confirmation switch settings can suppress rejected items, control required PO-item checks
and customer-specific outbound behavior.
6. Functional Incident Triage Matrix
Symptom Functional validation Likely owner / action
Consignment red light EDLNOT 35 timing; MB58; 
withdrawals; transit; cockpit
SD/EAEDI investigate; 
sales/customer confirm stock
EDLNOT posting failure IDoc status; scheduling 
agreement; stock; customer 
switches
EAEDI/SD support; integration 
escalation if mapping
DON ASN missing number JIT Kanban Detail; delivery; 
switch; grouping type
Sales confirms ID; SD/EAEDI 
authorized fix
Sales order wrong partner E1EDKA1, EDPA/EDSDC, 
customer master
Master data / EAEDI setup 
owner
Order change rejected Tolerance profile, 
order/delivery status
Sales decides accept/reject; SD 
supports
Order confirmation failure CVAB output, PO item 
reference, partner and output 
switches
SD/EAEDI outbound owner 
subject to agreed scope SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
7. Support Scope and Handover Understanding
During KT, the internal EAEDI team retains primary intake and manually forwards suitable tickets 
to the external SAP SD support team. The longer-term target is direct intake by the external team 
with internal escalation for access-restricted or non-transferred topics. Inbound IDoc readiness is to 
be confirmed after KT/playback; outbound ASN/order-confirmation ownership was not fully 
finalized in the supplied discussion. Do not treat this draft as final RACI approval.
8. Open Points / Validation Checklist
 Confirm exact SAP transaction names: EDL monitor, order monitor, DON delivery creation, 
customer switch SM30 view and internal order types.
 Confirm actual technical IDoc/message types and variants for DON, EDLNOT and 
ORDERS/ORDCHG by customer/system.
 Obtain one anonymized end-to-end IDoc, scheduling agreement, delivery and ASN example for 
each process.
 Confirm whether all outbound ASN and order-confirmation tickets belong to the external team 
and when intake transition takes effect.
 Agree escalation matrix, change authorization, customer contact protocol, and evidence 
required in tickets.
 Validate consignment minimum-stock logic, cumulative reset procedure, and business sign-off 
ownership.
Appendix A. Presentation Evidence
Figure 1. Consignment Process (EDL)
Figure 2. Consignment processing ZVEDLMON SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
Figure 3. Consignment process: Cums
Figure 4. Customer switch framework for EDLNOT
Figure 5. SA ZV87 + ZV44 – DON Process SCHAEFFLER | SAP SD / EAEDI KNOWLEDGE TRANSFER
Internal working document • Based on KT transcript and presentation screenshots • 24 Oct 2026
